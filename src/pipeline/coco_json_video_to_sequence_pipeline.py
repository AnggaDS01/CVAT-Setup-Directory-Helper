from src.components.coco_src.modify_json_file import modify_json_file
from src.components.coco_src.coco_json_splitter import coco_json_split
from src.components.video_to_frames import video_to_frames

import glob
import os

# Pipeline utama untuk menjalankan proses dari awal hingga akhir
def coco_json_process_video_pipeline(
        project_path, 
        coco_json_filename, 
        video_path, 
        split_ratio, 
        random_split, 
        is_split, 
        seed, 
        ext
    ):
    """
    Processes a video pipeline using a COCO JSON file.

    Args:
        project_path (str): The path to the project directory.
        coco_json_filename (str): The filename of the COCO JSON file.
        video_path (str): The path to the video file.
        split_ratio (float): The ratio of data to be used for training.
        random_split (bool): Whether to split the data randomly or sequentially.
        is_split (bool): Whether to split the dataset.
        seed (int): The seed for random splitting.
        ext (str): The file extension.

    Returns:
        None
    """

    DATA_STORE_DIR_NAME = 'annotations'
    TRAIN_DIR_NAME = 'train'
    VALID_DIR_NAME = 'valid'

    # 1. Ambil file names di file json
    json_path = glob.glob(os.path.join(project_path, "**", coco_json_filename), recursive=True)[0]
    file_names_list = modify_json_file(json_path, ext)
    
    # 2. Ubah video menjadi sequence frames
    output_dir =  os.path.join(project_path, DATA_STORE_DIR_NAME)
    total_frames = len(file_names_list)
    video_to_frames(
        project_path=project_path,
        video_path=video_path, 
        output_dir=output_dir, 
        total_frames=total_frames, 
        file_names_list=file_names_list, 
        ext=ext
    )

    # 3. Split dataset
    if is_split:
        coco_json_split(
            project_path=project_path, 
            coco_json_filename=coco_json_filename,
            train_dir_name=TRAIN_DIR_NAME,
            valid_dir_name=VALID_DIR_NAME, 
            split_ratio=split_ratio, 
            random_split=random_split,
            seed=seed
        )
    else:
        print("\nSkipping splitting dataset...\n\n")
