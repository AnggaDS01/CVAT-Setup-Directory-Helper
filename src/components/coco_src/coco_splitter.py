from src.components.get_file_list import get_first_n_files
from functools import partial
from src.constants import *

import os
import random
import inspect
from pathlib import Path
from shutil import move

def move_file_with_check(image_file, image_dest):
    move(image_file, image_dest)

def move_images_and_labels(image_file, target_image_dir):
    """
    Fungsi untuk memindahkan gambar dan label yang sesuai jika file label ada.

    Parameters:
    - image_file (Path): Path ke file gambar.
    - target_image_dir (Path): Direktori target untuk gambar.
    """

    if image_file.exists():
        move_file_with_check(
            image_file,
            target_image_dir / image_file.name,
        )
    else:
        print(f"\t[WARNING] Label file for '{image_file.name}' not found.")

def batch_move_files(image_files, target_image_dir):
    """
    Batch memindahkan file gambar dan label menggunakan map untuk mempercepat proses.

    Parameters:
    - image_files (list of Path): Daftar file gambar yang akan diproses.
    - label_dir (Path): Direktori sumber untuk label.
    - target_image_dir (Path): Direktori target untuk gambar.
    - target_label_dir (Path): Direktori target untuk label.
    """
    # Menggunakan partial untuk mengurangi argumen yang dikirim ke map
    mover = partial(move_images_and_labels, target_image_dir=target_image_dir)
    
    # Proses semua file gambar dengan map
    list(map(mover, image_files))

def coco_split_dataset(
    images_labels_dir_path,
    split_ratio,
    random_split,
    seed 
) -> None:
    
    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())
    print(f'\nRunning {function_name} in {file_name_function}...')

    if split_ratio is None:
        print("\t[INFO] No splitting needed as split_ratio is set to None.\n")
        return
    
    train_images_dir = Path(os.path.join(images_labels_dir_path, TRAIN_DIR))
    val_images_dir = Path(os.path.join(images_labels_dir_path, VALID_DIR))
    test_images_dir = Path(os.path.join(images_labels_dir_path, TEST_DIR))

    # Buat directory jika belum ada
    for directory in [
        train_images_dir, val_images_dir, test_images_dir
    ]:
        os.makedirs(directory, exist_ok=True)

    image_files = [file for file in train_images_dir.glob("*.*") if IMAGE_EXTENSIONS_PATTERN.search(str(file))]

    train_ratio = split_ratio[0]
    val_ratio = split_ratio[1]
    test_ratio = round(max(1.0 - (split_ratio[0] + split_ratio[1]), 0), 4)
    total_ratio = round(sum((train_ratio, val_ratio, test_ratio)), 2) 

    train_size = int(round(len(image_files) * train_ratio, 0))
    val_size = int(round(len(image_files) * val_ratio, 0))
    test_size = int(round(len(image_files) * test_ratio, 0))

    if total_ratio != 1.0:
        raise ValueError("[ERROR] split_ratio must sum to 1.0.\n")

    if random_split:
        random.seed(seed)
        random.shuffle(image_files)

    train_files = image_files[:train_size]
    val_files = image_files[train_size:] if round(test_size, 2) == 0.0 else image_files[train_size:train_size + val_size]
    test_files = [] if round(test_size, 2) == 0.0 else image_files[train_size + val_size:]

    images_valid_check = get_first_n_files(dir_path=val_images_dir, n=1)
    if len(images_valid_check) == 0:
        # Panggil fungsi untuk setiap kategori data
        batch_move_files(train_files, train_images_dir)
        batch_move_files(val_files, val_images_dir)
        batch_move_files(test_files, test_images_dir)

    else:
        val_image_paths = val_images_dir.glob("*.*")
        test_image_paths = test_images_dir.glob("*.*")
        batch_move_files(val_image_paths, train_images_dir)
        batch_move_files(test_image_paths, train_images_dir)

        batch_move_files(train_files, train_images_dir)
        batch_move_files(val_files, val_images_dir)
        batch_move_files(test_files, test_images_dir)

    number_of_train_files = os.listdir(train_images_dir)
    number_of_val_files = os.listdir(val_images_dir)
    number_of_test_files = os.listdir(test_images_dir)
    
    print(f"\t[INFO] Dataset split completed.")
    print(f"\t\t[INFO] train ratio: {train_ratio}, {len(number_of_train_files)} files in train.")
    print(f"\t\t[INFO] val ratio: {val_ratio}, {len(number_of_val_files)} files in val.")
    print(f"\t\t[INFO] test ratio: {test_ratio}, {len(number_of_test_files)} files in test.\n")

    return