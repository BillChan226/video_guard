import json

with open("/scratch/czr/video_guard/result/chatunivi.json") as f:
    data_list = json.load(f)

acc_count = 0
overall_count = 0
TP = 0
FP = 0
FN = 0

for idx, item in enumerate(data_list):
    response_list = data_list[item]["predictions"]

    for prediction in response_list:
        response = prediction["response"]
        label = prediction["label"]
        ground_truth = prediction["ground_truth"]
        if "yes" in response or "Yes" in response:
            if ground_truth == True:
                TP += 1
                acc_count += 1
            else:
                FP += 1
        else:
            if ground_truth == True:
                FN += 1
        overall_count += 1

accuracy = acc_count / overall_count
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1_score}")
