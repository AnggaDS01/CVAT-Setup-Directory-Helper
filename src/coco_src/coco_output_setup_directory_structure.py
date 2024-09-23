import os

def coco_json_setup_directory_structure(project_path):
    target_rename_folder = 'annotations'

    # Path ke folder annotations dan file JSON
    annotations_dir = os.path.join(project_path, target_rename_folder)
    train_dir = os.path.join(project_path, 'train')

    # Pastikan folder annotations ada
    if os.path.exists(train_dir):
        print(f"Folder {train_dir} sudah dibuat.")
        return

    # Rename folder annotations menjadi train
    os.rename(annotations_dir, train_dir)
    
    print("Folder berhasil diubah.")