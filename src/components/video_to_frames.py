from src.components.get_file_list import get_first_n_files

from tqdm import tqdm
import os
import inspect
import cv2
import inspect

# Fungsi untuk mengubah video menjadi sequence frames
def extract_frames_from_video(
    video_target_name_path,
    output_dir_path,
    fps,
    images_ext,
    image_size
) -> None:
    """
    Function to extract frames from a video and save them as images.

    Parameters:
    - video_target_name_path (str): Path to the target video file.
    - fps (int, optional): Frames per second to extract. Default is 30.
    - images_ext (str, optional): File extension for the output images. Default is 'jpg'.
    - image_size (tuple, optional): Size of the output images as (width, height).
      If set to None, the original frame size will be used.

    Returns:
    None
    """

    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())
    print(f'\nRunning {function_name} in {file_name_function}...')
    
    # Check if output directory exists, if not, create it
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path, exist_ok=True)

    # Check if images_store_dir_path contains any image files
    # image_in_dir = get_first_n_files(dir_path=output_dir_path, images_ext=images_ext, n=1)
    image_in_dir = get_first_n_files(dir_path=output_dir_path, n=1)
    if image_in_dir:
        print(f"\t[INFO] The video '{video_target_name_path}' has been extracted.")
        return

    # Capture the video
    video_cap = cv2.VideoCapture(str(video_target_name_path))
    
    # Get total number of frames
    total_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get the original FPS of the video
    original_fps = video_cap.get(cv2.CAP_PROP_FPS)
    
    # Print a warning if the requested fps is higher than the video's original fps
    if fps > original_fps:
        print(f"[WARNING] The requested fps ({fps}) is higher than the video's original fps ({original_fps}). "
              "You cannot extract more frames than what the video contains. Using the original fps instead.")
        fps = original_fps

    # Calculate how many frames to skip based on the desired FPS
    frame_interval = int(original_fps / fps) if fps <= original_fps else 1

    # Calculate total frames to be extracted
    total_extracted_frames = total_frames // frame_interval

    frame_count = 0
    extracted_frame_count = 0
    
    # Use tqdm to show progress
    with tqdm(total=total_extracted_frames, desc="Extracting frames", unit=" frame") as pbar:
        while True:
            success, frame = video_cap.read()
            
            if not success:
                break
            
            # Only save frames at the desired interval
            if frame_count % frame_interval == 0:
                # Resize the frame if image_size is specified, otherwise keep original size
                if image_size is not None:
                    frame = cv2.resize(frame, image_size, interpolation=cv2.INTER_CUBIC)
                
                # Construct image file name
                image_file_name = f"{output_dir_path.name}_{extracted_frame_count:05d}.{images_ext}"
                image_file_path = os.path.join(output_dir_path, image_file_name)
                
                frame_copy = frame.copy()

                # Save the image
                cv2.imwrite(image_file_path, frame)

                extracted_frame_count += 1
            
            frame_count += 1
            pbar.update(1)  # Update tqdm progress bar
    
    # Release video capture
    video_cap.release()

    print(f"\t[INFO] Extraction complete! {extracted_frame_count} frames saved to {output_dir_path}.")
    print(f"\t[INFO] Extracted image: with size {frame_copy.shape}.")
    print(f"\t[INFO] With {fps} FPS.")

    return