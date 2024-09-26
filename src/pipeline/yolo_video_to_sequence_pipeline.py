from src.components.get_file_names_from_txt import get_file_names_from_txt
from src.components.video_to_frames import video_to_frames
from src.components.yolo_src.yolo_setup_directory_structure import setup_directory_structure
from src.components.yolo_src.update_yaml import update_data_yaml
from src.components.yolo_src.yolo_splitter import yolo_split

import os
import glob

# Pipeline utama untuk menjalankan proses dari awal hingga akhir
def yolo_process_video_pipeline(
        project_path, 
        source_filename, 
        video_path, 
        project_name, 
        split_ratio, 
        random_split,
        seed, 
        is_split, 
        ext
    ):

    DATA_STORE_DIR_NAME = 'annotations'
    TRAIN_DIR_NAME = 'train'
    VALID_DIR_NAME = 'valid'
    IMAGES_DIR_NAME = 'images'
    LABELS_DIR_NAME = 'labels'

    # 1. Setup folder dan pindahkan label
    setup_directory_structure(
        project_path=project_path, 
        data_store_dir_name=DATA_STORE_DIR_NAME, 
        images_dir_name=IMAGES_DIR_NAME, 
        labels_dir_name=LABELS_DIR_NAME
    )
    
    # 2. Baca nama file dari train.txt
    file_names_path = glob.glob(os.path.join(project_path, "**", source_filename), recursive=True)[0]
    file_names_list = get_file_names_from_txt(file_names_path)
    
    # 3. Ubah video menjadi sequence frames
    output_dir = os.path.join(project_path, DATA_STORE_DIR_NAME, IMAGES_DIR_NAME)
    total_frames = len(file_names_list)
    video_to_frames(
        video_path=video_path, 
        output_dir=output_dir, 
        total_frames=total_frames, 
        file_names_list=file_names_list, 
        ext=ext
    )

    #4. Update data.yaml
    update_data_yaml(
        base_dir=project_path, 
        project_name=project_name, 
        data_store_dir=DATA_STORE_DIR_NAME, 
        train_dir_name=TRAIN_DIR_NAME, 
        valid_dir_name=VALID_DIR_NAME, 
        images_dir=IMAGES_DIR_NAME
    )

    # 5. Split dataset
    if is_split:
        yolo_split(
            project_path=project_path, 
            data_store_dir=DATA_STORE_DIR_NAME, 
            train_dir_name=TRAIN_DIR_NAME, 
            valid_dir_name=VALID_DIR_NAME, 
            images_dir_name=IMAGES_DIR_NAME, 
            labels_dir_name=LABELS_DIR_NAME, 
            split_ratio=split_ratio, 
            random_split=random_split,
            seed=seed,
            ext=ext
        )
    else:
        print("Skipping splitting dataset...")