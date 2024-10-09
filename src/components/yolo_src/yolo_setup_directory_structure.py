import os
import shutil
import inspect

# Fungsi untuk membuat folder baru dan memindahkan file
def setup_directory_structure(
        project_path, 
        data_store_dir_name, 
        images_dir_name, 
        labels_dir_name
    ):
    """
    Sets up the directory structure for a project by creating the necessary folders and moving files to their respective directories.

    Parameters:
        project_path (str): The path to the project directory.
        data_store_dir_name (str): The name of the directory where the data will be stored.
        images_dir_name (str): The name of the directory where the images will be stored.
        labels_dir_name (str): The name of the directory where the labels will be stored.

    Returns:
        None
    """
    
    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())

    print(f'\n\nRunning {function_name} di file {file_name_function}...')

    annotations_dir = os.path.join(project_path, data_store_dir_name)

    # Memindahkan file dari 'labels/train/' ke 'train/labels/'
    old_labels_dir = os.path.join(project_path, 'labels', 'train')
    new_labels_dir = os.path.join(annotations_dir, labels_dir_name)
    images_dir_name = os.path.join(annotations_dir, images_dir_name)

    if not os.path.exists(old_labels_dir):
        print(f"\tFolder {old_labels_dir} sudah dihapus.")
        return

    # Membuat folder 'train/images' dan 'train/labels'
    os.makedirs(images_dir_name, exist_ok=True)
    os.makedirs(new_labels_dir, exist_ok=True)
    
    for file_name in os.listdir(old_labels_dir):
        old_file_path = os.path.join(old_labels_dir, file_name)
        new_file_path = os.path.join(new_labels_dir, file_name)
        shutil.move(old_file_path, new_file_path)

    # Menghapus folder 'labels' yang kosong
    shutil.rmtree(os.path.join(project_path, 'labels'))
    
    print("\tFolder berhasil diubah.")