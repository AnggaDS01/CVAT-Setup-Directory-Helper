from src.components.display_function_name import display_function_name
from src.components.setup_images_directory import setup_images_dir
from src.constants import *

from pathlib import Path
import os
import inspect

def pascal_voc_setup_directory_structure(
        input_images_dir,
        is_video,
        image_size
    ) -> None:

    display_function_name(inspect.currentframe())

    output_images_dir = Path(os.path.join(input_images_dir, TRAIN_DIR))

    setup_images_dir(
        input_images_dir, 
        output_images_dir, 
        image_size, 
        is_video
    )

    return