import sys
import os
import subprocess

text_file_path = sys.argv[1]
video_directory = sys.argv[2]
flac_full_directory = sys.argv[3]
flac_cut_directory = sys.argv[4]

video_files = os.listdir(video_directory)
id = []

with open(text_file_path, 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) >= 2:
            id.append(parts[0])

#
def time_to_seconds(time_str):
    minutes, seconds = map(float, time_str.split(":"))
    return minutes * 60 + seconds

def seconds_to_time(seconds):
    minutes = int(seconds // 60)
    seconds %= 60
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{minutes:02d}:{int(seconds):02d}.{milliseconds:03d}"

def subtract_times(time1, time2):
    seconds1 = time_to_seconds(time1)
    seconds2 = time_to_seconds(time2)
    difference = seconds2 - seconds1
    return seconds_to_time(difference)
#

for video_file in video_files:
    video_name, video_extension = os.path.splitext(video_file)
    video_path = os.path.join(video_directory, video_file)
    flac_full_data = os.path.join(flac_full_directory, f"{video_name}.flac")
    
    def convert_mp4_to_flac(input_file, output_file):
        command = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "flac", "-y", output_file]
        subprocess.run(command)

    convert_mp4_to_flac(video_path, flac_full_data)
    print(video_path, flac_full_data)
    if video_name in id:
        with open(text_file_path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                parts = line.strip().split('\t')
                if len(parts) == 8 and parts[0] == video_name:
                    time_head = parts[2]
                    time_tail = parts[6]
                    duration_time = subtract_times(time_head, time_tail)

                    text_id = parts[1]
                    output_filename = f"{text_id}.flac"
                    flac_cut_data = os.path.join(flac_cut_directory, output_filename)

                    ffmpeg_command = [
                        "ffmpeg",
                        "-i", flac_full_data,
                        "-ss", time_head,
                        "-t", duration_time,
                        "-c", "copy",
                        "-y", flac_cut_data
                    ]

                    subprocess.run(ffmpeg_command)

                    print(f"Cut {video_file} to {flac_full_data} to {flac_cut_data}")

