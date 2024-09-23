import re

# Fungsi untuk membaca nama file dari 'train.txt'
def get_file_names_from_txt(file_names_path):
    file_names = []
    with open(file_names_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            file_name = line.strip().split('/')[-1]
            match = re.match(r'(\w+)\.?(png|jpe?g|webp|gif|bmp|tiff|heic)?', file_name, re.IGNORECASE)
            if match:
                file_names.append(match.group(1))
    return file_names