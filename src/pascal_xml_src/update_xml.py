from src.pascal_xml_src.modify_xml_file import modify_xml_file
from tqdm import tqdm

import glob
import os

def update_xml_files(project_path, new_extension):
    xml_files = glob.glob(os.path.join(project_path, "**", '*.xml'), recursive=True)

    # Loop dengan progress bar menggunakan tqdm
    modified_files = 0
    for xml_file in tqdm(xml_files, desc="Processing XML files"):
        modified = modify_xml_file(xml_file, new_extension)
        if modified:
            modified_files += 1

    print(f"\nTotal file yang diubah: {modified_files} dari {len(xml_files)} file XML.")