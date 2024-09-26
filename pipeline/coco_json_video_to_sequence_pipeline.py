from src.coco_src.modify_json_file import modify_json_file
from src.coco_src.coco_json_splitter import coco_json_split
from src.video_to_frames import video_to_frames

import glob
import os

# Pipeline utama untuk menjalankan proses dari awal hingga akhir
def coco_json_process_video_pipeline(project_path, coco_json_filename, video_path, split_ratio=0.8, random_split=True, is_split=True, seed=42, ext='jpg'):
    # 1. Ambil file names di file json
    json_path = glob.glob(os.path.join(project_path, "**", coco_json_filename), recursive=True)[0]
    file_names_list = modify_json_file(json_path, ext)
    
    # 2. Ubah video menjadi sequence frames
    output_dir =  os.path.join(project_path, 'annotations')
    total_frames = len(file_names_list)
    video_to_frames(video_path, output_dir, total_frames, file_names_list, ext)

    # 3. Split dataset
    if is_split:
        coco_json_split(
            project_path, 
            coco_json_filename, 
            split_ratio, 
            random_split,
            seed
        )
    else:
        print("Skipping splitting dataset...")
