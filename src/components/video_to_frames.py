from moviepy.editor import VideoFileClip
from tqdm import tqdm
import os
import re
import inspect
import glob

# Fungsi untuk mengubah video menjadi sequence frames
def video_to_frames(
        project_path,
        video_path, 
        output_dir, 
        total_frames, 
        file_names_list, 
        ext
    ):
    """
    Converts a video into a sequence of frames.

    Args:
        video_path (str): The path to the input video file.
        output_dir (str): The directory where the output frames will be saved.
        total_frames (int): The total number of frames to extract from the video.
        file_names_list (list): A list of file names for the output frames.
        ext (str): The file extension for the output frames.

    Returns:
        None
    """
    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())

    print(f'\nRunning {function_name} di file {file_name_function}...')

    # Check if output_dir contains any image files
    image_in_dir = glob.glob(os.path.join(project_path, '**', f'*.{ext}'), recursive=True)

    if image_in_dir:
        print(f"\tVideo '{video_path}' sudah terekstraksi.")
        return

    # Pastikan folder output ada
    os.makedirs(output_dir, exist_ok=True)

    # Membaca video
    clip = VideoFileClip(video_path)
    
    # Hitung FPS berdasarkan jumlah frame dan durasi video
    duration = clip.duration  # Durasi video dalam detik
    fps = total_frames / duration  # FPS yang dibutuhkan
    
    # Loop untuk menyimpan frame ke folder
    for i in tqdm(range(total_frames), desc="Extracting frames"):
        frame_time = i / fps
        frame_filename = os.path.join(output_dir, f"{file_names_list[i]}.{ext}")
        clip.save_frame(frame_filename, frame_time)
    
    print(f"\tVideo berhasil diubah menjadi {total_frames} frames di folder: {output_dir}")