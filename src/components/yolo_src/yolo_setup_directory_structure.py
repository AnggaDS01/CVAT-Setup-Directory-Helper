from src.constants import *
from pathlib import Path
from tqdm import tqdm
import os
import shutil
import inspect
import cv2
# Fungsi untuk membuat folder baru dan memindahkan file
def yolo_setup_directory_structure(
        images_store_dir_path,
        is_video,
        image_size
    ) -> None:
    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())
    print(f'\nRunning {function_name} in {file_name_function}...')

    output_images_dir = Path(os.path.join(images_store_dir_path, TRAIN_DIR, IMAGES_DIR))
    output_labels_dir = Path(os.path.join(images_store_dir_path, TRAIN_DIR, LABELS_DIR))
    
    if not os.path.exists(output_images_dir):
        os.makedirs(output_images_dir, exist_ok=True)
        print(f"\t[INFO] The directory '{output_images_dir}' was created successfully.")
    else:
        print(f"\t[INFO] The directory '{output_images_dir}' has been created.")

    if os.listdir(output_images_dir):
        print(f"\t\t[INFO] The directory '{output_images_dir}' is not empty. Skipping...")
    else:
        is_consider_resize = (not is_video) and (image_size is not None)
        # move all files in images_store_dir_path to output_images_dir
        for filename in tqdm(os.listdir(images_store_dir_path), total=len(os.listdir(images_store_dir_path)) - 1, desc=f"Resize to {image_size} and Moving images" if is_consider_resize else "Moving images"):
            if IMAGE_EXTENSIONS_PATTERN.search(filename):
                img_path = os.path.join(images_store_dir_path, filename)
                if is_consider_resize:
                    # Baca gambar
                    img = cv2.imread(img_path)
                    img = cv2.resize(img, (image_size[0], image_size[1]), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(img_path, img)
                shutil.move(img_path, output_images_dir)
        print(f"\t\t[INFO] The images files are moved from '{images_store_dir_path}' to '{output_images_dir}'.")

    if not os.path.exists(output_labels_dir):
        os.makedirs(output_labels_dir, exist_ok=True)
        print(f"\t[INFO] The directory '{output_labels_dir}' was created successfully.")
    else:
        print(f"\t[INFO] The directory '{output_labels_dir}' has been created.")

    if os.listdir(output_labels_dir):
        print(f"\t\t[INFO] The directory '{output_labels_dir}' is not empty. Skipping...")
    else:
        # Looping semua file dalam directory
        for filename in os.listdir(output_images_dir):
            if IMAGE_EXTENSIONS_PATTERN.search(filename):
                # Ambil nama file tanpa ekstensi
                txt_filename = os.path.splitext(filename)[0] + '.txt'
                # Buat file .txt kosong
                txt_file_path = os.path.join(output_labels_dir, txt_filename)
                open(txt_file_path, 'w').close()  # Buat file txt kosong
        print(f"\t\t[INFO] The labels files are created.")

    return