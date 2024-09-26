from moviepy.editor import VideoFileClip
from tqdm import tqdm
import os
import re

# Fungsi untuk mengubah video menjadi sequence frames
def video_to_frames(
        video_path, 
        output_dir, 
        total_frames, 
        file_names_list, 
        ext
    ):

    # Check if output_dir contains any image files
    image_extensions = re.compile(r'\.(png|jpe?g|webp|gif|bmp|tiff|heic)$', re.IGNORECASE)
    files_in_dir = os.listdir(output_dir)
    if any(image_extensions.search(file) for file in files_in_dir):
        print(f"Folder {output_dir} sudah ada file gambar.")
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
    
    print(f"Video berhasil diubah menjadi {total_frames} frames di folder: {output_dir}")