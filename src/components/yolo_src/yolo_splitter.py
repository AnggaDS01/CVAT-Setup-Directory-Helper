from src.components.display_function_name import display_function_name
from src.components.split_helper import batch_move_files, split_settings, display_info_split
from functools import partial
from src.constants import *

import os
import random
import inspect
from pathlib import Path

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