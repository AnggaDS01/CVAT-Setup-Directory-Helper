from src.components.get_file_list import get_first_n_files
from src.constants import *
from functools import partial
from shutil import move
import random
import os

def move_file_with_check(image_file, image_dest, label_file=None, label_dest=None, format_data="yolo") -> None:
    """Move an image file to a target directory, and if label_file and
    label_dest is given, move the label file to the target directory as well.

    Args:
        image_file (str): Path to the image file.
        image_dest (str): Path to the target directory for the image file.
        label_file (str): Path to the label file. Defaults to None.
        label_dest (str): Path to the target directory for the label file. Defaults to None.
        format_data (str): Format of the data. Defaults to "yolo".

    Returns:
        None
    """
    
    move(image_file, image_dest)

    if format_data == "yolo" and label_file and label_dest:
        move(label_file, label_dest)

    return

def move_images_and_labels(image_file, target_image_dir, label_dir=None, target_label_dir=None, format_data="yolo") -> None:
    """
    Move an image file to a target directory.

    Parameters:
        image_file (Path): The path to the image file to be moved.
        target_image_dir (Path): The path to the directory where the image file will be moved.
        label_dir (Path): The path to the directory containing the labels corresponding to the image file.
        target_label_dir (Path): The path to the directory where the labels will be moved.
        format_data (str): The format of the dataset, either 'yolo' or 'pascal_voc' or 'coco'.
    
    Returns:
        None
    """

    # Check if the specified image file exists
    if image_file.exists():
        # Set up label file paths if format is YOLO
        if format_data == "yolo":
            label_file = label_dir / f"{image_file.stem}.txt" if label_dir else None
            label_dest = target_label_dir / f"{image_file.stem}.txt" if target_label_dir else None
        else:
            label_file, label_dest = None, None

        # Move both image and label files to target locations
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
    """
    Move a list of image files to a target directory.

    Parameters:
        image_files (list): A list of Path objects pointing to the image files to be moved.
        target_image_dir (Path): The path to the directory where the image files will be moved.
        format_data (str): The format of the dataset, either 'yolo' or 'pascal_voc' or 'coco'.
        label_dir (Path): The path to the directory containing labels corresponding to the image files.
        target_label_dir (Path): The path to the directory where the labels will be moved.

    Returns:
        None
    """

    # Prepare partial function for moving individual files with specific parameters
    mover = partial(
        move_images_and_labels,
        target_image_dir=target_image_dir,
        label_dir=label_dir,
        target_label_dir=target_label_dir,
        format_data=format_data
    )
    
    # Apply the move function to each file in the list
    list(map(mover, image_files))

    return

def split_settings(
        train_images_dir,
        val_images_dir,
        split_ratio, 
        random_split, 
        seed
    ):
    """
    Split a list of image files into training, validation, and test sets.

    Parameters:
        train_images_dir (Path): The path to the directory containing images to be split.
        val_images_dir (Path): The path to the directory containing validation images.
        split_ratio (tuple): The ratio for splitting the dataset (e.g., (0.8, 0.1) for train and validation).
        random_split (bool): Whether to randomly split the dataset.
        seed (int): Seed for random splitting.

    Returns:
        tuple: A tuple containing the following:

            * train_files (list): A list of files in the training set.
            * train_ratio (float): The ratio of the training set.
            * val_files (list): A list of files in the validation set.
            * val_ratio (float): The ratio of the validation set.
            * test_files (list): A list of files in the test set.
            * test_ratio (float): The ratio of the test set.
            * images_valid_check (list): A list containing one file from the validation set to check if it exists.
    """

    # Get all image files in the training directory that match the specified image extension pattern
    image_files = [file for file in train_images_dir.glob("*.*") if IMAGE_EXTENSIONS_PATTERN.search(str(file))]

    # Define individual ratios for training, validation, and test sets
    train_ratio = split_ratio[0]
    val_ratio = split_ratio[1]
    test_ratio = round(max(1.0 - (train_ratio + val_ratio), 0), 4)  # Calculate remaining ratio for test set
    
    # Verify the total ratio equals 1.0; raise an error if not
    total_ratio = round(sum((train_ratio, val_ratio, test_ratio)), 2)
    if total_ratio != 1.0:
        raise ValueError("[ERROR] split_ratio must sum to 1.0.\n")
    
    # Determine the number of images in each split based on the calculated ratios
    train_size = int(round(len(image_files) * train_ratio, 0))
    val_size = int(round(len(image_files) * val_ratio, 0))
    test_size = int(round(len(image_files) * test_ratio, 0))

    # Randomly shuffle the image files if random_split is enabled
    if random_split:
        random.seed(seed)
        random.shuffle(image_files)

    # Split the files into training, validation, and test sets based on calculated sizes
    train_files = image_files[:train_size]
    val_files = image_files[train_size:] if test_size == 0 else image_files[train_size:train_size + val_size]
    test_files = [] if test_size == 0 else image_files[train_size + val_size:]

    # Check if validation images exist in the specified directory for confirmation
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
    
    """
    Displays information about the dataset split.

    Parameters:
        train_images_dir (Path): The path to the directory containing the training images.
        val_images_dir (Path): The path to the directory containing the validation images.
        test_images_dir (Path): The path to the directory containing the test images.
        train_ratio (float): The ratio of the training set.
        val_ratio (float): The ratio of the validation set.
        test_ratio (float): The ratio of the test set.

    Returns:
        None
    """

    # Get the number of files in each directory for the split overview
    number_of_train_files = os.listdir(train_images_dir)
    number_of_val_files = os.listdir(val_images_dir)
    number_of_test_files = os.listdir(test_images_dir)
    
    # Display the split information for user reference
    print(f"\t[INFO] Dataset split completed.")
    print(f"\t\t[INFO] Train ratio: {train_ratio}, {len(number_of_train_files)} files in {train_images_dir}.")
    print(f"\t\t[INFO] Validation ratio: {val_ratio}, {len(number_of_val_files)} files in {val_images_dir}.")
    print(f"\t\t[INFO] Test ratio: {test_ratio}, {len(number_of_test_files)} files in {test_images_dir}.\n")

    return