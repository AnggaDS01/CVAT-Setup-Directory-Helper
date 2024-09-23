from src.coco_src.coco_output_setup_directory_structure import coco_json_setup_directory_structure
from src.coco_src.modify_json_file import modify_json_file
from src.video_to_frames import video_to_frames

import glob
import os

# Pipeline utama untuk menjalankan proses dari awal hingga akhir
def json_process_video_pipeline(project_path, video_path, ext="jpg"):
    # 1. Setup folder dan pindahkan label
    coco_json_setup_directory_structure(project_path)
    
    # 2. Ambil file names di file json
    json_path = glob.glob(os.path.join(project_path, "**", '*.json'), recursive=True)[0]
    file_names_list = modify_json_file(json_path, ext)
    
    # 3. Ubah video menjadi sequence frames
    output_dir =  os.path.join(project_path, 'train')
    total_frames = len(file_names_list)
    video_to_frames(video_path, output_dir, total_frames, file_names_list, ext)