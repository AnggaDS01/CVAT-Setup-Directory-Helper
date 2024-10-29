from src.components.yolo_src.yolo_setup_labels_directory import yolo_setup_labels_dir

from src.components.display_function_name import display_function_name
from src.components.setup_images_directory import setup_images_dir
from src.constants import *

from pathlib import Path
import os
import inspect

# Fungsi untuk membuat folder baru dan memindahkan file
def yolo_setup_directory_structure(
        input_images_dir,
        is_video,
        image_size
    ) -> None:

    """
    Sets up the directory structure for YOLO format.

    This function processes the source path and its content according to the chosen format
    for object detection datasets. It supports YOLO format.

    Parameters:
        input_images_dir (Path): The path to the source directory containing videos or images.
        is_video (bool): Whether the input is a video or not.
        image_size (tuple): The desired size for the output images.

    Returns:
        None
    """
    
    display_function_name(inspect.currentframe())

    output_images_dir = Path(os.path.join(input_images_dir, TRAIN_DIR, IMAGES_DIR))
    output_labels_dir = Path(os.path.join(input_images_dir, TRAIN_DIR, LABELS_DIR))
    
    setup_images_dir(
        input_images_dir, 
        output_images_dir, 
        image_size, 
        is_video
    )

    yolo_setup_labels_dir(
        output_labels_dir, 
        output_images_dir
    )

    return