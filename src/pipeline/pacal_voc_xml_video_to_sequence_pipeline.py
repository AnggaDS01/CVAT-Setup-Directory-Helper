from src.components.get_file_names_from_txt import get_file_names_from_txt
from src.components.video_to_frames import video_to_frames
from src.components.pascal_xml_src.pascal_voc_setup_directory_structure import pascal_xml_setup_directory_structure
from src.components.pascal_xml_src.update_xml import update_xml_files
from src.components.pascal_xml_src.pascal_voc_splitter import pascal_voc_split

import os
import glob

# Pipeline utama untuk menjalankan proses dari awal hingga akhir
def xml_process_video_pipeline(
        project_path, 
        source_filename, 
        video_path, 
        split_ratio, 
        random_split, 
        seed, 
        is_split, 
        ext
    ):

    DATA_STORE_DIR_NAME = 'annotation'
    TRAIN_DIR_NAME = 'train'
    VALID_DIR_NAME = 'valid'
 
    # 1. Setup folder dan pindahkan label
    pascal_xml_setup_directory_structure(
        project_path=project_path, 
        data_store_dir_name=DATA_STORE_DIR_NAME, 
        source_filename=source_filename
    )
    
    # 2. Baca nama file dari train.txt
    file_names_path = glob.glob(os.path.join(project_path, "**", source_filename), recursive=True)[0]
    file_names_list = get_file_names_from_txt(file_names_path)
    
    # 3. Ubah video menjadi sequence frames
    output_dir =  os.path.join(project_path, DATA_STORE_DIR_NAME)
    total_frames = len(file_names_list)
    video_to_frames(
        video_path=video_path, 
        output_dir=output_dir, 
        total_frames=total_frames, 
        file_names_list=file_names_list, 
        ext=ext
    )

    # 4. Update xml files
    update_xml_files(
        project_path=project_path, 
        data_store_dir=DATA_STORE_DIR_NAME, 
        new_extension=ext
    )

    # 5. Split dataset
    if is_split:
        pascal_voc_split(
            project_path=project_path, 
            data_store_dir=DATA_STORE_DIR_NAME, 
            train_dir_name=TRAIN_DIR_NAME, 
            valid_dir_name=VALID_DIR_NAME, 
            split_ratio=split_ratio, 
            random_split=random_split, 
            seed=seed, 
            ext=ext
        )
    else:
        print("Skipping splitting dataset...")