import sys
import cv2
import os

text_file_path = sys.argv[1]
video_directory = sys.argv[2]
image_directory = sys.argv[3]

video_files = os.listdir(video_directory)
id = []

with open(text_file_path, 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) >= 2:
            id.append(parts[0])

for video_file in video_files:
    video_name, video_extension = os.path.splitext(video_file)

    if video_name in id:
        video_path = os.path.join(video_directory, video_file)
        timestamps = []

        with open(text_file_path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                parts = line.strip().split('\t')
                if parts[0] == video_name:
                    timestamps.extend([(parts[i], parts[i + 1]) for i in range(2, len(parts), 2)])

        os.makedirs(image_directory, exist_ok=True)

        cap = cv2.VideoCapture(video_path)

        for timestamp, filename_prefix in timestamps:
            minutes, seconds = map(float, timestamp.split(':'))
            total_seconds = minutes * 60 + seconds

            cap.set(cv2.CAP_PROP_POS_MSEC, total_seconds * 1000)

            ret, frame = cap.read()

            if ret:
                output_filename = f"{filename_prefix}.jpg"
                output_path = os.path.join(image_directory, output_filename)
                cv2.imwrite(output_path, frame)
                print(f"Saved {output_filename} for {video_file}")
            else:
                print(f"Failed to capture frame at {timestamp} for {video_file}")

        cap.release()
    else:
        print(f"No matching text file found for {video_file}")
    