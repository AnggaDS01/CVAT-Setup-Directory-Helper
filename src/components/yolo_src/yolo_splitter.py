from src.components.display_function_name import display_function_name
from src.components.split_helper import batch_move_files, split_settings, display_info_split
from functools import partial
from src.constants import *

import os
import random
import inspect
from pathlib import Path
from shutil import move

def yolo_split_dataset(
    images_labels_dir_path,
    split_ratio,
    random_split,
    seed 
) -> None:
    """
    Split for a YOLO dataset of images and labels into training, validation, and testing sets.

    Parameters:
        images_labels_dir_path (Path): The path to the directory where the images and labels are stored.
        split_ratio (tuple): A tuple of two floats that sums to 1.0 (train, val) or None, but if you give it like (0.8, 0.1), it will automatically calculate the ratio for the test set.
            to be used for training, validation, and testing, respectively. If None, no splitting is done.
        random_split (bool): Whether to split the data randomly or sequentially. Defaults to True.
        seed (int): The seed for random splitting. Defaults to 42.

    Returns:
        None
    """
    display_function_name(inspect.currentframe())

    if split_ratio is None:
        print("\t[INFO] No splitting needed as split_ratio is set to None.\n")
        return

    train_images_dir = Path(os.path.join(images_labels_dir_path, TRAIN_DIR, IMAGES_DIR))
    val_images_dir = Path(os.path.join(images_labels_dir_path, VALID_DIR, IMAGES_DIR))
    test_images_dir = Path(os.path.join(images_labels_dir_path, TEST_DIR, IMAGES_DIR))

    train_labels_dir = Path(os.path.join(images_labels_dir_path, TRAIN_DIR, LABELS_DIR))
    val_labels_dir = Path(os.path.join(images_labels_dir_path, VALID_DIR, LABELS_DIR))
    test_labels_dir = Path(os.path.join(images_labels_dir_path, TEST_DIR, LABELS_DIR))

    # Buat directory jika belum ada
    for directory in [
        train_images_dir, val_images_dir, test_images_dir, train_labels_dir, val_labels_dir, test_labels_dir
    ]:
        os.makedirs(directory, exist_ok=True)

    (
        train_files, 
        train_ratio, 
        val_files, 
        val_ratio, 
        test_files,
        test_ratio,
        images_valid_check
    ) = split_settings(
        train_images_dir=train_images_dir,
        val_images_dir=val_images_dir,
        split_ratio=split_ratio,
        random_split=random_split,
        seed=seed
    )

    format_data = "yolo"

    if len(images_valid_check) == 0:
        # Panggil fungsi untuk setiap kategori data
        batch_move_files(image_files=train_files, target_image_dir=train_images_dir, format_data=format_data)
        batch_move_files(image_files=val_files, target_image_dir=val_images_dir, format_data=format_data)
        batch_move_files(image_files=test_files, target_image_dir=test_images_dir, format_data=format_data)

    else:
        val_image_paths = val_images_dir.glob("*.*")
        test_image_paths = test_images_dir.glob("*.*")

        batch_move_files(image_files=val_image_paths, target_image_dir=train_images_dir, format_data=format_data)
        batch_move_files(image_files=test_image_paths, target_image_dir=train_images_dir, format_data=format_data)

        batch_move_files(image_files=train_files, target_image_dir=train_images_dir, format_data=format_data)
        batch_move_files(image_files=val_files, target_image_dir=val_images_dir, format_data=format_data)
        batch_move_files(image_files=test_files, target_image_dir=test_images_dir, format_data=format_data)

    display_info_split(
        train_images_dir,
        val_images_dir,
        test_images_dir,
        train_ratio,
        val_ratio,
        test_ratio
    )
    
    return

# # Filter hanya file yang cocok dengan ekstensi gambar
# image_files = [file for file in train_images_dir.glob("*.*") if IMAGE_EXTENSIONS_PATTERN.search(str(file))]

# # Hitung ukuran split
# train_ratio = split_ratio[0]
# val_ratio = split_ratio[1]
# test_ratio = round(max(1.0 - (split_ratio[0] + split_ratio[1]), 0), 4)
# total_ratio = round(sum((train_ratio, val_ratio, test_ratio)), 2) 

# train_size = int(round(len(image_files) * train_ratio, 0))
# val_size = int(round(len(image_files) * val_ratio, 0))
# test_size = int(round(len(image_files) * test_ratio, 0))
# # print(train_size, val_size, test_size, sum((train_size, val_size, test_size)), total_ratio)

# # Validasi jumlah split ratio
# if total_ratio != 1.0:
#     raise ValueError("[ERROR] split_ratio must sum to 1.0.\n")

# if random_split:
#     random.seed(seed)
#     random.shuffle(image_files)

# train_files = image_files[:train_size]
# val_files = image_files[train_size:] if round(test_size, 2) == 0.0 else image_files[train_size:train_size + val_size]
# test_files = [] if round(test_size, 2) == 0.0 else image_files[train_size + val_size:]

# images_valid_check = get_first_n_files(dir_path=val_images_dir, n=1)


# # Fungsi untuk memindahkan file dengan pengecekan jika file sudah dipindahkan
# def move_file_with_check(image_file, image_dest, label_file, label_dest):
#     move(image_file, image_dest)
#     move(label_file, label_dest)

# def move_images_and_labels(image_file, label_dir, target_image_dir, target_label_dir):
#     """
#     Fungsi untuk memindahkan gambar dan label yang sesuai jika file label ada.

#     Parameters:
#     - image_file (Path): Path ke file gambar.
#     - label_dir (Path): Direktori sumber untuk label.
#     - target_image_dir (Path): Direktori target untuk gambar.
#     - target_label_dir (Path): Direktori target untuk label.
#     """
    
#     label_file = label_dir / f"{image_file.stem}.txt"  # Label file dengan ekstensi .txt
#     if image_file.exists():
#         move_file_with_check(
#             image_file,
#             target_image_dir / image_file.name,
#             label_file,
#             target_label_dir / label_file.name
#         )
#     else:
#         print(f"\t[WARNING] Label file for '{image_file.name}' not found.")

# def batch_move_files(image_files, label_dir, target_image_dir, target_label_dir):
#     """
#     Batch memindahkan file gambar dan label menggunakan map untuk mempercepat proses.

#     Parameters:
#     - image_files (list of Path): Daftar file gambar yang akan diproses.
#     - label_dir (Path): Direktori sumber untuk label.
#     - target_image_dir (Path): Direktori target untuk gambar.
#     - target_label_dir (Path): Direktori target untuk label.
#     """
#     # Menggunakan partial untuk mengurangi argumen yang dikirim ke map
#     mover = partial(move_images_and_labels, label_dir=label_dir, target_image_dir=target_image_dir, target_label_dir=target_label_dir)
    
#     # Proses semua file gambar dengan map
#     list(map(mover, image_files))
