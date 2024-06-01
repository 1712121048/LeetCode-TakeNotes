import subprocess
import os

def get_video_duration(file_path):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path], stdout=subprocess.PIPE, text=True)
    return float(result.stdout)

def main():
    video_folder = 'D:\脑语者\脑语者语法'

    total_duration = 0

    for filename in os.listdir(video_folder):
        if filename.endswith('.mp4'):
            file_path = os.path.join(video_folder, filename)
            duration = int(get_video_duration(file_path))
            total_duration += duration

            print(f"{filename}: {duration:.2f} seconds")

    total_duration_minutes = total_duration / 60
    print(f"\nTotal Duration: {total_duration_minutes:.2f} minutes")

if __name__ == "__main__":
    main()
