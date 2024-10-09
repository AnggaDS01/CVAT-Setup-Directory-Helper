import re
import inspect

# Fungsi untuk membaca nama file dari 'train.txt'
def get_file_names_from_txt(file_names_path):
    """
    Retrieves a list of file names from a given text file.

    Args:
        file_names_path (str): The path to the text file containing file names.

    Returns:
        list: A list of file names extracted from the text file.
    """
    ...
    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())

    print(f'\nRunning {function_name} di file {file_name_function}...')

    file_names = []
    with open(file_names_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            file_name = line.strip().split('/')[-1]
            match = re.match(r'(\w+)\.?(png|jpe?g|webp|gif|bmp|tiff|heic)?', file_name, re.IGNORECASE)
            if match:
                file_names.append(match.group(1))
    return file_names