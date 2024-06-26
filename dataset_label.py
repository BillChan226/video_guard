import os
import json

# Define the folder containing the videos
video_folder = "dataset"
output_file = "video_labels.json"

# Define the available labels and their abbreviations
label_abbreviations = {
    "si": "Sexual implication",
    "scs": "Sexual content (Subtle)",
    "sce": "Sexual content (Evident)",
    "h": "Harassment",
    "vh": "Violence & Harm",
    "di": "Deceptive Information",
    "ia": "Illegal & Anti-social",
    "t": "Terrorism",
    "na": "None",
}

def get_video_files(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.mp4')]

def convert_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def get_user_input(video_file):
    input_data = {}
    overall_labels = set()
    while True:
        start_time = input(f"Enter start timestamp (minute:second) for {video_file} (or 'done' to finish): ")
        if start_time.lower() == 'done':
            break
        end_time = input(f"Enter end timestamp (minute:second) for start time {start_time}: ")
        label_input = input(f"Enter label abbreviations for start time {start_time} (separated by spaces, choose from {list(label_abbreviations.keys())}): ")
        labels = label_input.split()

        valid_labels = []
        for label in labels:
            if label in label_abbreviations:
                valid_labels.append(label_abbreviations[label])
                overall_labels.add(label_abbreviations[label])
            else:
                print(f"Invalid label '{label}'. Choose from {list(label_abbreviations.keys())}.")

        start_seconds = convert_to_seconds(start_time)
        end_seconds = convert_to_seconds(end_time)
        
        if start_seconds not in input_data:
            input_data[start_seconds] = []

        input_data[start_seconds].append({
            "start_time": start_seconds,
            "labels": valid_labels,
            "end_time": end_seconds
        })
    
    return input_data, list(overall_labels)

def main():
    video_files = get_video_files(video_folder)
    all_labels = {}
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            all_labels = json.load(f)

    for idx, video_file in enumerate(video_files):
        if idx < 8:
            continue
        print(f"Processing video: {video_file}")
        video_labels, overall_labels = get_user_input(video_file)
        all_labels[video_file] = {
            "timestamps": video_labels,
            "overall_labels": overall_labels
        }

        with open(output_file, 'w') as f:
            json.dump(all_labels, f, indent=4)
        print(f"Labels saved to {output_file}")

if __name__ == "__main__":
    main()
