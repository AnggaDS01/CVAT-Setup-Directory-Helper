import json
import inspect
from tqdm import tqdm

def modify_json_file(json_path, new_extension):
    """
    Modifies a JSON file by changing the file extension of all image files.

    Args:
        json_path (str): The path to the JSON file to be modified.
        new_extension (str): The new file extension to be applied to all image files.

    Returns:
        list: A list of file names without extensions.
    """
    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())

    print(f'\n\nRunning {function_name} di file {file_name_function}...')

    with open(json_path, 'r') as file:
        data = json.load(file)

    # Flag untuk mengecek apakah ada perubahan
    changed = False

    file_names_list = []
    for value in tqdm(data['images'], desc="Processing JSON file"):
        filename = value['file_name']
        base_name = filename.rsplit('.', 1)[0]
        current_ext = filename.rsplit('.', 1)[1]

        # Hanya ubah jika ekstensi saat ini bukan ekstensi baru
        if current_ext.lower() != new_extension.lower():
            value['file_name'] = f"{base_name}.{new_extension}"
            changed = True  # Tanda bahwa ada perubahan

        file_names_list.append(base_name)
        value['file_name'] = f"{base_name}.{new_extension}"

    # Jika ada perubahan, dump data kembali ke file JSON
    if changed:
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=4)
        print("\tFile JSON telah diperbarui.")
    else:
        print("\tTidak ada perubahan pada file JSON.")

    return file_names_list