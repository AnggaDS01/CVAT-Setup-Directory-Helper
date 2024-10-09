import os
import random
import shutil
import inspect
from pathlib import Path
from tqdm import tqdm

def yolo_split(
        project_path, 
        data_store_dir, 
        train_dir_name, 
        valid_dir_name, 
        images_dir_name, 
        labels_dir_name, 
        split_ratio, 
        random_split, 
        seed, 
        ext
    ):
    """
    Splits a dataset of images and labels into training and validation sets.

    Parameters:
        project_path (str): The path to the project directory.
        data_store_dir (str): The directory where the images and labels are stored.
        train_dir_name (str): The name of the directory where the training data will be stored.
        valid_dir_name (str): The name of the directory where the validation data will be stored.
        images_dir_name (str): The name of the directory where the images are stored.
        labels_dir_name (str): The name of the directory where the labels are stored.
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

    # Path ke folder images dan labels
    images_dir = os.path.join(project_path, data_store_dir, images_dir_name)
    labels_dir = os.path.join(project_path, data_store_dir, labels_dir_name)

    # Path ke folder train dan valid
    train_images_dir = os.path.join(project_path, train_dir_name, images_dir_name)
    valid_images_dir = os.path.join(project_path, valid_dir_name, images_dir_name)
    train_labels_dir = os.path.join(project_path, train_dir_name, labels_dir_name)
    valid_labels_dir = os.path.join(project_path, valid_dir_name, labels_dir_name)

    if os.path.exists(train_images_dir) or os.path.exists(valid_images_dir):
        print(f"\tFolder:\n \t\t1. {Path(train_images_dir).parent} \n \t\t2. {Path(valid_images_dir).parent} \n\tsudah dibuat. Hapus folder tersebut jika ingin memulai ulang.\n\n")
        return
    
    # Buat folder train dan valid jika belum ada
    os.makedirs(train_images_dir, exist_ok=True)
    os.makedirs(valid_images_dir, exist_ok=True)
    os.makedirs(train_labels_dir, exist_ok=True)
    os.makedirs(valid_labels_dir, exist_ok=True)

    # Pastikan folder images dan labels ada
    if not os.path.exists(images_dir) or not os.path.exists(labels_dir):
        raise FileNotFoundError("Folder images atau labels tidak ditemukan di path yang diberikan.")

    # Ambil daftar semua file gambar dan label
    image_files = sorted([f for f in os.listdir(images_dir) if f.endswith(f'.{ext}')])
    label_files = sorted([f for f in os.listdir(labels_dir) if f.endswith('.txt')])

    # Pastikan jumlah file gambar dan label sesuai
    if len(image_files) != len(label_files):
        raise ValueError("Jumlah file gambar dan label tidak sama.")

    # Pilih splitting secara acak atau berurutan
    if random_split:
        random.seed(seed)
        combined = list(zip(image_files, label_files))
        random.shuffle(combined)  # Splitting secara acak
        image_files, label_files = zip(*combined)

    # Tentukan indeks untuk splitting
    split_index = int(len(image_files) * split_ratio)
    
    # Membagi file gambar dan label menjadi train dan valid
    train_images, valid_images = image_files[:split_index], image_files[split_index:]
    train_labels, valid_labels = label_files[:split_index], label_files[split_index:]

    def copy_files(images_list, labels_list, target_images_dir, target_labels_dir, target_dir_name):
        # Copy file gambar dan label ke folder train
        for img_file, lbl_file in tqdm(zip(images_list, labels_list), desc=f"Copying {target_dir_name} files", total=len(images_list)):
            # Copy gambar
            shutil.copyfile(os.path.join(images_dir, img_file), os.path.join(target_images_dir, img_file))
            # Copy label
            shutil.copyfile(os.path.join(labels_dir, lbl_file), os.path.join(target_labels_dir, lbl_file))

    copy_files(train_images, train_labels, train_images_dir, train_labels_dir, train_dir_name)
    copy_files(valid_images, valid_labels, valid_images_dir, valid_labels_dir, valid_dir_name)

    print(f"\tSplitting selesai. Data train: {len(train_images)} gambar, Data valid: {len(valid_images)} gambar.\n\n")