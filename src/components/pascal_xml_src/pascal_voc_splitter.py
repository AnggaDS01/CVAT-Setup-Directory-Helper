import os
import shutil
import random
import inspect
from tqdm import tqdm
from pathlib import Path

def pascal_voc_split(
        project_path, 
        data_store_dir, 
        train_dir_name, 
        valid_dir_name,
        split_ratio, 
        random_split, 
        seed, 
        ext
    ):
    """
    Splits a dataset of images and annotations into training and validation sets.

    Parameters:
        project_path (str): The path to the project directory.
        data_store_dir (str): The directory where the images and annotations are stored.
        train_dir_name (str): The name of the directory where the training data will be stored.
        valid_dir_name (str): The name of the directory where the validation data will be stored.
        split_ratio (float): The ratio of data to be used for training.
        random_split (bool): Whether to split the data randomly or sequentially.
        seed (int): The seed for random splitting.
        ext (str): The file extension of the images.

    Returns:
        None
    """

    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())

    print(f'\nRunning {function_name} di file {file_name_function}...')

    annotations_dir = os.path.join(project_path, data_store_dir)

    # Membuat folder train dan valid jika belum ada
    train_dir = os.path.join(project_path, train_dir_name)
    valid_dir = os.path.join(project_path, valid_dir_name)

    if os.path.exists(train_dir) or os.path.exists(valid_dir):
        print(f"\tFolder:\n \t\t1. {Path(train_dir).parent} \n \t\t2. {Path(valid_dir).parent} \n\tsudah dibuat. Hapus folder tersebut jika ingin memulai ulang.\n\n")
        return

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)

    # Ambil semua file gambar (.jpg) dari folder annotations
    files = [f for f in os.listdir(annotations_dir) if f.endswith(f".{ext}")]

    # Random shuffle file jika random_split=True
    if random_split:
        random.seed(seed)
        random.shuffle(files)

    # Tentukan jumlah file untuk training
    num_train = int(len(files) * split_ratio)

    # Bagi file menjadi train dan valid
    train_files = files[:num_train]
    valid_files = files[num_train:]

    def copy_files(file_list, target_dir, target_dir_name):
        """Menyalin file gambar dan xml ke direktori target"""
        for file in tqdm(file_list, desc=f"Copying {target_dir_name} files"):
            # Nama file jpg dan file xml yang sesuai
            image_file = file
            xml_file = file.replace(f".{ext}", ".xml")
            
            # Salin file jpg dan xml ke folder target
            shutil.copy2(os.path.join(annotations_dir, image_file), os.path.join(target_dir, image_file))
            shutil.copy2(os.path.join(annotations_dir, xml_file), os.path.join(target_dir, xml_file))

    # Salin file ke folder train dan validasi
    copy_files(train_files, train_dir, train_dir_name)
    copy_files(valid_files, valid_dir, valid_dir_name)

    print(f"\tSplitting selesai. Data train: {len(train_files)} gambar, Data valid: {len(valid_files)} gambar.\n\n")