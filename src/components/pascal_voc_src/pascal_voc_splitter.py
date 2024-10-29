from src.components.display_function_name import display_function_name
from src.components.split_helper import batch_move_files, split_settings, display_info_split
from src.constants import *

import os
import inspect
from pathlib import Path

def pascal_voc_split_dataset(
    input_images_dir,
    split_ratio,
    random_split,
    seed
) -> None:
    
    """
    Splits the dataset into training, validation, and test sets for Pascal VOC format.

    This function sets up the directory structure for the dataset and splits the images
    according to the specified split ratio. If the dataset is already split, it moves the files
    back to the training set and re-splits them. It also displays information about the split process.

    Parameters:
        input_images_dir (Path): The path to the directory containing images to be split.
        split_ratio (tuple): The ratio for splitting the dataset (e.g., (0.8, 0.1) for train and validation).
        random_split (bool): Whether to randomly split the dataset.
        seed (int): Seed for random splitting.

    Returns:
        None
    """
    
    display_function_name(inspect.currentframe())

    if split_ratio is None:
        print("\t[INFO] No splitting needed as split_ratio is set to None.\n")
        return
    
    train_images_dir = Path(os.path.join(input_images_dir, TRAIN_DIR))
    val_images_dir = Path(os.path.join(input_images_dir, VALID_DIR))
    test_images_dir = Path(os.path.join(input_images_dir, TEST_DIR))

    for directory in [
        train_images_dir, val_images_dir, test_images_dir
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

    if len(images_valid_check) == 0:
        batch_move_files(image_files=train_files, target_image_dir=train_images_dir, format_data=None)
        batch_move_files(image_files=val_files, target_image_dir=val_images_dir, format_data=None)
        batch_move_files(image_files=test_files, target_image_dir=test_images_dir, format_data=None)
    else:
        val_image_paths = val_images_dir.glob("*.*")
        test_image_paths = test_images_dir.glob("*.*")

        batch_move_files(image_files=val_image_paths, target_image_dir=train_images_dir, format_data=None)
        batch_move_files(image_files=test_image_paths, target_image_dir=train_images_dir, format_data=None)

        batch_move_files(image_files=train_files, target_image_dir=train_images_dir, format_data=None)
        batch_move_files(image_files=val_files, target_image_dir=val_images_dir, format_data=None)
        batch_move_files(image_files=test_files, target_image_dir=test_images_dir, format_data=None)

    display_info_split(
        train_images_dir,
        val_images_dir,
        test_images_dir,
        train_ratio,
        val_ratio,
        test_ratio
    )