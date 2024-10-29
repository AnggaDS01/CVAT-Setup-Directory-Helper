from src.components.get_file_list import get_first_n_files
from src.components.display_function_name import display_function_name

from tqdm import tqdm
import os
import inspect
import cv2
import inspect

def extract_frames_from_video(
    video_target_name_path,
    output_dir_path,
    fps,
    images_ext,
    image_size
) -> None:
    """
    Extracts frames from a video at a specified frame rate and saves them as images to a target directory.

    Args:
        video_target_name_path (Path): The path to the video file to be extracted.
        output_dir_path (Path): The path to the directory where extracted frames will be saved.
        fps (int): The desired frame rate at which to extract frames.
        images_ext (str): The file extension for the extracted images (e.g. 'jpg', 'png', etc.).
        image_size (tuple or None): If specified, the size to which the extracted frames will be resized.

    Returns:
        None
    """
    
    # Display the function name for tracking purposes
    display_function_name(inspect.currentframe())
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path, exist_ok=True)

    # Check if frames are already extracted in the directory
    image_in_dir = get_first_n_files(dir_path=output_dir_path, n=1)
    if image_in_dir:
        print(f"\t[INFO] The video '{video_target_name_path}' has already been extracted.")
        return

    # Initialize video capture object
    video_cap = cv2.VideoCapture(str(video_target_name_path))
    total_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    original_fps = video_cap.get(cv2.CAP_PROP_FPS)
    
    # Check if requested FPS is higher than the video FPS, adjust if necessary
    if fps > original_fps:
        print(f"[WARNING] The requested FPS ({fps}) exceeds the video's original FPS ({original_fps}). "
              "Using the original FPS instead.")
        fps = original_fps

    # Calculate frame interval based on the target FPS
    frame_interval = int(original_fps / fps) if fps <= original_fps else 1
    total_extracted_frames = total_frames // frame_interval

    # Initialize counters for frame extraction process
    frame_count = 0
    extracted_frame_count = 0
    
    # Display progress bar during frame extraction
    with tqdm(total=total_extracted_frames, desc="Extracting frames", unit=" frame") as pbar:
        while True:
            success, frame = video_cap.read()
            
            # Break if no more frames can be read from the video
            if not success:
                break
            
            # Extract frame based on the interval calculated
            if frame_count % frame_interval == 0:
                # Resize frame if a target size is specified
                if image_size is not None:
                    frame = cv2.resize(frame, image_size, interpolation=cv2.INTER_CUBIC)
                
                # Construct a unique file name for each frame
                image_file_name = f"{output_dir_path.name}_{extracted_frame_count:05d}.{images_ext}"
                image_file_path = os.path.join(output_dir_path, image_file_name)
                
                # Copy and save the frame to the specified path
                frame_copy = frame.copy()
                cv2.imwrite(image_file_path, frame)

                extracted_frame_count += 1
            
            # Update frame counter and progress bar
            frame_count += 1
            pbar.update(1) 
    
    # Release video capture resources
    video_cap.release()

    # Log extraction details after completion
    print(f"\t[INFO] Extraction complete! {extracted_frame_count} frames saved to {output_dir_path}.")
    print(f"\t[INFO] Sample extracted frame size: {frame_copy.shape}.")
    print(f"\t[INFO] Extraction FPS used: {fps}.")
    
    return