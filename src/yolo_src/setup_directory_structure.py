import os
import shutil

# Fungsi untuk membuat folder baru dan memindahkan file
def setup_directory_structure(project_path):
    train_dir = os.path.join(project_path, 'train')
    
    if os.path.exists(train_dir):
        print(f"Folder {train_dir} sudah dibuat.")
        return

    # Membuat folder 'train/images' dan 'train/labels'
    os.makedirs(os.path.join(train_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(train_dir, 'labels'), exist_ok=True)
    
    # Memindahkan file dari 'labels/train/' ke 'train/labels/'
    old_labels_dir = os.path.join(project_path, 'labels', 'train')
    new_labels_dir = os.path.join(train_dir, 'labels')
    
    for file_name in os.listdir(old_labels_dir):
        old_file_path = os.path.join(old_labels_dir, file_name)
        new_file_path = os.path.join(new_labels_dir, file_name)
        shutil.move(old_file_path, new_file_path)

    # Menghapus folder 'labels' yang kosong
    shutil.rmtree(os.path.join(project_path, 'labels'))
    
    print("Folder berhasil diubah.")