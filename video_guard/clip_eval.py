import torch
import clip
import numpy as np
from PIL import Image
import os
import pandas as pd
import urllib
import warnings

warnings.filterwarnings('ignore')

device = "cuda"

flags_map = {
    "Sexual implication": "this image contain sexual implication, where no explicit sexual content is shown but implied.",
    "Subtle sexual content": "this image contain subtle sexual content, where a small amount of sexual content is shown.",
    "Evident sexual content": "this image contain evident sexual content, where an extensive amount of sexual content is shown.",
    "Harassment": "this image contain harassment, where the content is intended to harass or bully an individual or group.",
    "Violence & Harm": "this image contain violence or harm, where the content is intended to cause harm or injury to an individual or group.",
    "Deceptive Information": "this image contain deceptive information, where the content is intended to deceive or mislead viewers.",
    "Illegal & Anti-social": "this image contain illegal or anti-social content.",
    "Terrorism": "this image incite terrorism, where the content encourages violent and anti-social behaviors.",
    "Neutral": "this image is clean and safe.",
}

clip_model, clip_preprocess = clip.load("ViT-B/32", device=device)

def detect_moderation_label(image_path, safe_flag, flags_map, threshold):
    # Preprocess the image
    image_processed = clip_preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    
    # Prepare flags for moderation
    flags = list(flags_map.keys())
    flags_tokenized = clip.tokenize(flags).to(device)
    
    # Extract features from the CLIP model
    with torch.no_grad():
        image_features = clip_model.encode_image(image_processed)
        text_features = clip_model.encode_text(flags_tokenized)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        
        stacked_text_features = []
        for i in range(text_features.shape[0] - 1):
            stacked_text_features.append(text_features[[i, -1], :].T.unsqueeze(0))
        stacked_text_features = torch.vstack(stacked_text_features)
        
        softmax_probs = (100 * image_features @ stacked_text_features).softmax(dim=-1).cpu()
    
    # Find the maximum probability and corresponding label
    max_prob, index = softmax_probs[:, :, 0].max().numpy().tolist(), softmax_probs[:, :, 0].argmax().numpy()

    print(max_prob, index)
    
    # Check if the maximum probability exceeds the threshold
    if max_prob > threshold:
        return flags_map.get(flags[index]), max_prob
    return flags_map.get(safe_flag), threshold

# Generate moderation labels
image_path = "/scratch/czr/video_guard/video_guard/test.png"
safe_flag = "Neutral"
threshold = 0.95

labels, max_prob = detect_moderation_label(image_path=image_path, safe_flag=safe_flag, flags_map=flags_map, threshold=threshold)

print(labels)
