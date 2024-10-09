import os
import shutil
import glob
import inspect

def pascal_xml_setup_directory_structure(
        project_path, 
        data_store_dir_name, 
        source_filename
    ):
    """
    Sets up the directory structure for Pascal VOC XML files.

    This function takes in the project path, data store directory name, and source filename.
    It creates the necessary directories, moves XML files to the correct location, and removes any unnecessary folders.

    Parameters:
        project_path (str): The path to the project directory.
        data_store_dir_name (str): The name of the directory to store the data.
        source_filename (str): The filename of the source file.

    Returns:
        None
    """
    
    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())

    print(f'\n\nRunning {function_name} di file {file_name_function}...')

    target_delete_folder_1 = 'Annotations'
    target_delete_folder_2 = 'ImageSets'

    # Membuat folder 'train' di dalam folder baru 'traffic-pascalVOC'
    annotations_dir = os.path.join(project_path, data_store_dir_name)
    
    if os.path.exists(annotations_dir):
        print(f"\tFolder {annotations_dir} sudah dibuat.")
        return
    
    os.makedirs(annotations_dir, exist_ok=True)

    # Pindahkan file .xml dari 'annotations/' ke 'train/'
    xml_files = glob.glob(os.path.join(project_path, "**", '*.xml'), recursive=True)
    for xml_file in xml_files:
        shutil.move(xml_file, annotations_dir)

    # Pindahkan 'default.txt' dari 'ImageSets/Main/' ke direktori utama 'traffic-pascalVOC'
    file_names_path = glob.glob(os.path.join(project_path, "**", source_filename), recursive=True)[0]
    if os.path.exists(file_names_path):
        shutil.move(file_names_path, project_path)

    # Hapus folder lama jika sudah tidak diperlukan
    shutil.rmtree(os.path.join(project_path, target_delete_folder_1))
    shutil.rmtree(os.path.join(project_path, target_delete_folder_2))

    print("\tFolder berhasil diubah.")