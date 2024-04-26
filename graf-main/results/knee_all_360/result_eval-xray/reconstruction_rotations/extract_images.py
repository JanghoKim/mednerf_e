import cv2
import os

def extract_frames(video_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture video from file
    cap = cv2.VideoCapture(video_path)
    count = 0

    while True:
        # Read a new frame
        success, frame = cap.read()
        if not success:
            break  # If no frame is read, break the loop

        # Save frame as JPEG file
        frame_filename = f"{output_folder}/frame_{count:04d}.jpg"
        cv2.imwrite(frame_filename, frame)
        print(f"Saved {frame_filename}")
        count += 1

    # Release the capture once everything is done
    cap.release()
    print(f"Extracted {count} frames from the video.")

# Example usage
video_path = '0000_rgb.mp4'
output_folder = 'extracted_frames'
extract_frames(video_path, output_folder)