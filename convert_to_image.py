import os

import cv2


def extract_first_50_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    frame_count = 0
    while frame_count < 100:
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video or cannot read frame.")
            break

        filename = os.path.join(output_folder, f"frame{frame_count+1}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        frame_count += 1

    cap.release()
    print("Done.")

if __name__ == "__main__":
    video_path = "/Users/saugatsingh/Downloads/soccer_tracker-master/data/Screen Recording 2025-04-20 at 12.05.48 AM.mov"          # <- replace with your video path
    output_folder = "data/output_frames"        # <- folder where frames will be saved
    extract_first_50_frames(video_path, output_folder)
