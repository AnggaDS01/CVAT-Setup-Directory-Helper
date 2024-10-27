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
    
    if not os.path.exists(output_images_dir):
        os.makedirs(output_images_dir, exist_ok=True)
        print(f"\t[INFO] The directory '{output_images_dir}' was created successfully.")
    else:
        print(f"\t[INFO] The directory '{output_images_dir}' has been created.")

    if os.listdir(output_images_dir):
        print(f"\t\t[INFO] The directory '{output_images_dir}' is not empty. Skipping...")
    else:
        is_consider_resize = (not is_video) and (image_size is not None)
        # move all files in input_images_dir to output_images_dir
        for filename in tqdm(os.listdir(input_images_dir), total=len(os.listdir(input_images_dir)) - 1, desc=f"Resize to {image_size} and Moving images" if is_consider_resize else "Moving images"):
            if IMAGE_EXTENSIONS_PATTERN.search(filename):
                img_path = os.path.join(input_images_dir, filename)
                if is_consider_resize:
                    img = cv2.imread(img_path)
                    img = cv2.resize(img, (image_size[0], image_size[1]), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(img_path, img)
                move(img_path, output_images_dir)
        print(f"\t\t[INFO] The images files are moved from '{input_images_dir}' to '{output_images_dir}'.")