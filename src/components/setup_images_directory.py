from src.constants import *

from tqdm import tqdm
from shutil import move
import os
import cv2

def setup_images_dir(
        input_images_dir, 
        output_images_dir, 
        image_size, 
        is_video
    ) -> None:
    
    """
    Sets up the directory structure for images.

    This function moves all files in input_images_dir to output_images_dir, and if image_size is specified and is_video is False, it resizes the images to the specified size.

    Parameters:
        input_images_dir (Path): The path to the directory containing the images.
        output_images_dir (Path): The path to the directory where the images will be saved.
        image_size (tuple): The desired size for the output images.
        is_video (bool): Whether the input is a video or not.

    Returns:
        None
    """
    
    # Check if the output directory exists; if not, create it
    if not os.path.exists(output_images_dir):
        os.makedirs(output_images_dir, exist_ok=True)
        print(f"\t[INFO] The directory '{output_images_dir}' was created successfully.")
    else:
        print(f"\t[INFO] The directory '{output_images_dir}' already exists.")
    
    # Check if the output directory is empty; if not, skip moving files
    if os.listdir(output_images_dir):
        print(f"\t\t[INFO] The directory '{output_images_dir}' is not empty. Skipping...")
    else:
        # Decide whether resizing is required based on input type (video or image) and provided size
        is_consider_resize = (not is_video) and (image_size is not None)
        
        # Move all matching image files from the input directory to the output directory
        for filename in tqdm(
            os.listdir(input_images_dir), 
            total=len(os.listdir(input_images_dir)) - 1, 
            desc=f"Resizing to {image_size} and moving images" if is_consider_resize else "Moving images"
        ):
            # Process files with matching image extensions only
            if IMAGE_EXTENSIONS_PATTERN.search(filename):
                img_path = os.path.join(input_images_dir, filename)
                
                # Resize image if conditions are met
                if is_consider_resize:
                    img = cv2.imread(img_path)
                    img = cv2.resize(img, (image_size[0], image_size[1]), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(img_path, img)
                
                # Move file to the output directory
                move(img_path, output_images_dir)
        
        print(f"\t\t[INFO] Image files moved from '{input_images_dir}' to '{output_images_dir}'.")