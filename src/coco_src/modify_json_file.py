import json
from tqdm import tqdm

def modify_json_file(json_path, new_extension):
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
        print("File JSON telah diperbarui.")
    else:
        print("Tidak ada perubahan pada file JSON.")

    return file_names_list