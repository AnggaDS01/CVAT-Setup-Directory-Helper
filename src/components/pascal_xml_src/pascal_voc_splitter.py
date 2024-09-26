import os
import shutil
import random
from tqdm import tqdm

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

    annotations_dir = os.path.join(project_path, data_store_dir)

    # Membuat folder train dan valid jika belum ada
    train_dir = os.path.join(project_path, train_dir_name)
    valid_dir = os.path.join(project_path, valid_dir_name)

    if os.path.exists(train_dir) or os.path.exists(valid_dir):
        print(f"Folder:\n 1. {train_dir} \n 2. {valid_dir} \nsudah dibuat. Hapus folder tersebut jika ingin memulai ulang.")
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
    num_train = int(len(files) * train_ratio)

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

    print(f"Dataset berhasil dibagi: {len(train_files)} untuk train dan {len(valid_files)} untuk validasi.")