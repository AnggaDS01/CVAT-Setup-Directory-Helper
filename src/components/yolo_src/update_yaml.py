from src.components.yolo_src.extract_classes_from_data_yaml import extract_classes_from_data_yaml

import os
import yaml
import inspect

# Fungsi untuk memperbarui data.yaml ke format YOLOv8
def update_data_yaml(
        base_dir, 
        project_name, 
        data_store_dir, 
        train_dir_name, 
        valid_dir_name, 
        images_dir
    ):
    """
    Updates the data.yaml file to the YOLOv8 format.

    Parameters:
        base_dir (str): The base directory of the project.
        project_name (str): The name of the project.
        data_store_dir (str): The directory where the data is stored.
        train_dir_name (str): The name of the training directory.
        valid_dir_name (str): The name of the validation directory.
        images_dir (str): The directory where the images are stored.

    Returns:
        None
    """
    
    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())

    print(f'\nRunning {function_name} di file {file_name_function}...')

    old_data_yaml_path = os.path.join(base_dir, 'data.yaml')
    
    # Baca kelas dari data.yaml yang sudah ada
    label_classes = extract_classes_from_data_yaml(old_data_yaml_path)
    
    # Buat path baru untuk train, val, dan test
    new_data = {
        'annotations': f'{project_name}/{data_store_dir}/{images_dir}',
        'train': f'{project_name}/{train_dir_name}/{images_dir}',
        'valid': f'{project_name}/{valid_dir_name}/{images_dir}',
        'nc': len(label_classes),  # Jumlah kelas
        'names': label_classes      # Daftar kelas
    }

    # Menulis file data.yaml baru dengan format blok (multi-line)
    with open(old_data_yaml_path, 'w') as yaml_file:
        yaml.dump(new_data, yaml_file, default_flow_style=False)  # Multi-line format
    
    print(f"\tdata.yaml berhasil diubah dan disimpan di: {old_data_yaml_path}")

