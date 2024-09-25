from src.get_file_names_from_txt import get_file_names_from_txt
from src.video_to_frames import video_to_frames
from src.pascal_xml_src.xml_output_setup_directory_structure import pascal_xml_setup_directory_structure
from src.pascal_xml_src.update_xml import update_xml_files

import os
import glob

# Pipeline utama untuk menjalankan proses dari awal hingga akhir
def xml_process_video_pipeline(project_path, video_path, source_filename, ext="jpg"):
    # 1. Setup folder dan pindahkan label
    pascal_xml_setup_directory_structure(project_path, source_filename)
    
    # 2. Baca nama file dari train.txt
    file_names_path = glob.glob(os.path.join(project_path, "**", source_filename), recursive=True)[0]
    file_names_list = get_file_names_from_txt(file_names_path)
    
    # 3. Ubah video menjadi sequence frames
    output_dir =  os.path.join(project_path, 'train')
    total_frames = len(file_names_list)
    video_to_frames(video_path, output_dir, total_frames, file_names_list, ext)

    # #4. Update xml files
    update_xml_files(project_path, ext)