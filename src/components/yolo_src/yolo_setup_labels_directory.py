from src.constants import *
import os

def yolo_setup_labels_dir(output_labels_dir, output_images_dir) -> None:
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