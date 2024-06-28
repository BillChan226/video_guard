import os
import json

def get_video_paths(folder):
    """Retrieve all mp4 files from the specified folder."""
    return [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith('.mp4')]

def get_labels():
    """Prompt user to input categories."""
    print("Enter categories (e.g., 1 2 4):")
    print("1 - C1(Sexual Content)")
    print("2 - C2(Harassment & Bullying)")
    print("3 - C3(Threats, Violence & Harm)")
    print("4 - C4(False & Deceptive Information)")
    print("5 - C5(Illegal/Regulated Activities)")
    print("6 - C6(Hateful Content & Extremism)")
    
    while True:
        try:
            labels = list(map(int, input("Enter categories: ").split()))
            if all(1 <= label <= 6 for label in labels):
                return labels
            else:
                print("Invalid input. Please enter numbers between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter valid numbers separated by spaces.")

def main(folder, output_file):
    """Main function to process videos and save labels."""
    video_paths = get_video_paths(folder)
    data = []

    for video_path in video_paths:
        print(f"Video path: {video_path}")
        labels = get_labels()
        data.append({"video_path": video_path, "labels": labels})

        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    folder = input("Enter the folder path containing the videos: ")
    output_file = "new_labels.json"
    main(folder, output_file)
    print(f"Labels saved to {output_file}")
