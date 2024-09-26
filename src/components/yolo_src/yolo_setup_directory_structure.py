import os
import shutil

# Fungsi untuk membuat folder baru dan memindahkan file
def setup_directory_structure(
        project_path, 
        data_store_dir_name, 
        images_dir_name, 
        labels_dir_name
    ):
    
    annotations_dir = os.path.join(project_path, data_store_dir_name)
    
    if os.path.exists(annotations_dir):
        print(f"Folder {annotations_dir} sudah dibuat.")
        return

    # Memindahkan file dari 'labels/train/' ke 'train/labels/'
    old_labels_dir = os.path.join(project_path, 'labels', 'train')
    new_labels_dir = os.path.join(annotations_dir, labels_dir_name)
    images_dir_name = os.path.join(annotations_dir, images_dir_name)

    # Membuat folder 'train/images' dan 'train/labels'
    os.makedirs(images_dir_name, exist_ok=True)
    os.makedirs(new_labels_dir, exist_ok=True)
    
    for file_name in os.listdir(old_labels_dir):
        old_file_path = os.path.join(old_labels_dir, file_name)
        new_file_path = os.path.join(new_labels_dir, file_name)
        shutil.move(old_file_path, new_file_path)

    # Menghapus folder 'labels' yang kosong
    shutil.rmtree(os.path.join(project_path, 'labels'))
    
    print("Folder berhasil diubah.")