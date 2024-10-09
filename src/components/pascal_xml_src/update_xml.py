from src.components.pascal_xml_src.modify_xml_file import modify_xml_file
from tqdm import tqdm

import glob
import os
import inspect

def update_xml_files(
        project_path, 
        data_store_dir, 
        new_extension
    ):
    """
    Updates XML files in a project directory by modifying their file extensions.

    Args:
        project_path (str): The path to the project directory.
        data_store_dir (str): The directory where the XML files are stored.
        new_extension (str): The new file extension to be applied to the XML files.

    Returns:
        None
    """

    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())

    print(f'\nRunning {function_name} di file {file_name_function}...')
    
    xml_files = glob.glob(os.path.join(project_path, data_store_dir, '*.xml'), recursive=True)

    # Loop dengan progress bar menggunakan tqdm
    modified_files = 0
    for xml_file in tqdm(xml_files, desc="Processing XML files"):
        modified = modify_xml_file(xml_file, new_extension)
        if modified:
            modified_files += 1

    print(f"\tTotal file yang diubah: {modified_files} dari {len(xml_files)} file XML.")