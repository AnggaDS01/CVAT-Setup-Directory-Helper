from src.get_file_names_from_txt import get_file_names_from_txt
from src.video_to_frames import video_to_frames
from src.yolo_src.yolo_setup_directory_structure import setup_directory_structure
from src.yolo_src.update_yaml import update_data_yaml
from src.yolo_src.yolo_splitter import yolo_split

import os
import glob

# Pipeline utama untuk menjalankan proses dari awal hingga akhir
def yolo_process_video_pipeline(project_path, source_filename, video_path, project_name, split_ratio=0.8, random_split=True, seed=42, is_split=True, ext='jpg'):
    DATA_STORE_DIR_NAME = 'annotations'
    TRAIN_DIR_NAME = 'train'
    VALID_DIR_NAME = 'valid'
    IMAGES_DIR_NAME = 'images'
    LABELS_DIR_NAME = 'labels'

    # 1. Setup folder dan pindahkan label
    setup_directory_structure(project_path, DATA_STORE_DIR_NAME, IMAGES_DIR_NAME, LABELS_DIR_NAME)
    
    # 2. Baca nama file dari train.txt
    file_names_path = glob.glob(os.path.join(project_path, "**", source_filename), recursive=True)[0]
    file_names_list = get_file_names_from_txt(file_names_path)
    
    # 3. Ubah video menjadi sequence frames
    output_dir = os.path.join(project_path, DATA_STORE_DIR_NAME, IMAGES_DIR_NAME)
    total_frames = len(file_names_list)
    video_to_frames(video_path, output_dir, total_frames, file_names_list, ext)

    #4. Update data.yaml
    update_data_yaml(project_path, project_name, DATA_STORE_DIR_NAME, TRAIN_DIR_NAME, VALID_DIR_NAME, IMAGES_DIR_NAME)

    # 5. Split dataset
    if is_split:
        yolo_split(
            project_path, 
            DATA_STORE_DIR_NAME, 
            TRAIN_DIR_NAME, 
            VALID_DIR_NAME, 
            IMAGES_DIR_NAME, 
            LABELS_DIR_NAME, 
            split_ratio, 
            random_split,
            seed,
            ext
        )
    else:
        print("Skipping splitting dataset...")