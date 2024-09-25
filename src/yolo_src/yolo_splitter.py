import os
import random
import shutil
from pathlib import Path
from tqdm import tqdm

def yolo_split(project_path, data_store_dir, train_dir_name, valid_dir_name, images_dir_name, labels_dir_name, split_ratio=0.8, random_split=True, ext='jpg'):
    # Path ke folder images dan labels
    images_dir = os.path.join(project_path, data_store_dir, images_dir_name)
    labels_dir = os.path.join(project_path, data_store_dir, labels_dir_name)

    # Path ke folder train dan valid
    train_images_dir = os.path.join(project_path, train_dir_name, images_dir_name)
    valid_images_dir = os.path.join(project_path, valid_dir_name, images_dir_name)
    train_labels_dir = os.path.join(project_path, train_dir_name, labels_dir_name)
    valid_labels_dir = os.path.join(project_path, valid_dir_name, labels_dir_name)

    if os.path.exists(train_images_dir) or os.path.exists(valid_images_dir):
        print(f"Folder:\n 1. {Path(train_images_dir).parent} \n 2. {Path(valid_images_dir).parent} \nsudah dibuat. Hapus folder tersebut jika ingin memulai ulang.")
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
        combined = list(zip(image_files, label_files))
        random.shuffle(combined)  # Splitting secara acak
        image_files, label_files = zip(*combined)

    # Tentukan indeks untuk splitting
    split_index = int(len(image_files) * split_ratio)
    
    # Membagi file gambar dan label menjadi train dan valid
    train_images, valid_images = image_files[:split_index], image_files[split_index:]
    train_labels, valid_labels = label_files[:split_index], label_files[split_index:]

    # Copy file gambar dan label ke folder train
    for img_file, lbl_file in tqdm(zip(train_images, train_labels), total=len(train_images), desc="Copying train files"):
        shutil.copyfile(os.path.join(images_dir, img_file), os.path.join(train_images_dir, img_file))
        shutil.copyfile(os.path.join(labels_dir, lbl_file), os.path.join(train_labels_dir, lbl_file))

    # Copy file gambar dan label ke folder valid
    for img_file, lbl_file in tqdm(zip(valid_images, valid_labels), total=len(valid_images), desc="Copying valid files"):
        shutil.copyfile(os.path.join(images_dir, img_file), os.path.join(valid_images_dir, img_file))
        shutil.copyfile(os.path.join(labels_dir, lbl_file), os.path.join(valid_labels_dir, lbl_file))

    print(f"Splitting selesai. Data train: {len(train_images)} gambar, Data valid: {len(valid_images)} gambar.")