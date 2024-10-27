from src.components.get_file_list import get_first_n_files
from src.constants import *
from functools import partial
from shutil import move
import random
import os

def move_file_with_check(image_file, image_dest, label_file=None, label_dest=None, format_data="yolo") -> None:
    # Pindahkan file gambar
    move(image_file, image_dest)

    # Pindahkan file label jika formatnya "yolo" dan label_file diberikan
    if format_data == "yolo" and label_file and label_dest:
        move(label_file, label_dest)

    return

def move_images_and_labels(image_file, target_image_dir, label_dir=None, target_label_dir=None, format_data="yolo") -> None:
    if image_file.exists():
        # Jika format adalah YOLO, tentukan file dan destinasi label
        if format_data == "yolo":
            label_file = label_dir / f"{image_file.stem}.txt" if label_dir else None
            label_dest = target_label_dir / f"{image_file.stem}.txt" if target_label_dir else None
        else:
            label_file, label_dest = None, None

        move_file_with_check(
            image_file,
            target_image_dir / image_file.name,
            label_file,
            label_dest,
            format_data
        )
    else:
        print(f"\t[WARNING] File '{image_file.name}' not found.")

    return

def batch_move_files(image_files, target_image_dir, format_data="yolo", label_dir=None, target_label_dir=None):
    # Menggunakan partial untuk mengurangi argumen yang dikirim ke map
    mover = partial(
        move_images_and_labels,
        target_image_dir=target_image_dir,
        label_dir=label_dir,
        target_label_dir=target_label_dir,
        format_data=format_data
    )
    
    # Proses semua file gambar dengan map
    list(map(mover, image_files))

    return

def split_settings(
        train_images_dir,
        val_images_dir,
        split_ratio, 
        random_split, 
        seed
    ):
    # Filter hanya file yang cocok dengan ekstensi gambar
    image_files = [file for file in train_images_dir.glob("*.*") if IMAGE_EXTENSIONS_PATTERN.search(str(file))]

    # Hitung ukuran split
    train_ratio = split_ratio[0]
    val_ratio = split_ratio[1]
    test_ratio = round(max(1.0 - (split_ratio[0] + split_ratio[1]), 0), 4)
    total_ratio = round(sum((train_ratio, val_ratio, test_ratio)), 2) 

    train_size = int(round(len(image_files) * train_ratio, 0))
    val_size = int(round(len(image_files) * val_ratio, 0))
    test_size = int(round(len(image_files) * test_ratio, 0))
    # print(train_size, val_size, test_size, sum((train_size, val_size, test_size)), total_ratio)

    # Validasi jumlah split ratio
    if total_ratio != 1.0:
        raise ValueError("[ERROR] split_ratio must sum to 1.0.\n")

    if random_split:
        random.seed(seed)
        random.shuffle(image_files)

    train_files = image_files[:train_size]
    val_files = image_files[train_size:] if round(test_size, 2) == 0.0 else image_files[train_size:train_size + val_size]
    test_files = [] if round(test_size, 2) == 0.0 else image_files[train_size + val_size:]

    images_valid_check = get_first_n_files(dir_path=val_images_dir, n=1)

    return (
        train_files, 
        train_ratio, 
        val_files, 
        val_ratio, 
        test_files,
        test_ratio,
        images_valid_check
    )

def display_info_split(
    train_images_dir,
    val_images_dir,
    test_images_dir,
    train_ratio,
    val_ratio,
    test_ratio
) -> None:
    
    number_of_train_files = os.listdir(train_images_dir)
    number_of_val_files = os.listdir(val_images_dir)
    number_of_test_files = os.listdir(test_images_dir)
    
    print(f"\t[INFO] Dataset split completed.")
    print(f"\t\t[INFO] train ratio: {train_ratio}, {len(number_of_train_files)} files in train.")
    print(f"\t\t[INFO] val ratio: {val_ratio}, {len(number_of_val_files)} files in val.")
    print(f"\t\t[INFO] test ratio: {test_ratio}, {len(number_of_test_files)} files in test.\n")

    return