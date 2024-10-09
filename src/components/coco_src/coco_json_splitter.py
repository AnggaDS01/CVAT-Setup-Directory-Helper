import os
import json
import random
import shutil
import glob
import inspect
from tqdm import tqdm
from pathlib import Path

def coco_json_split(
        project_path,
        coco_json_filename,
        train_dir_name,
        valid_dir_name,
        split_ratio,
        random_split,
        seed
    ):
    """
    Splits a COCO JSON file into training and validation sets.

    Parameters:
        project_path (str): The path to the project directory.
        coco_json_filename (str): The filename of the COCO JSON file.
        train_dir_name (str): The name of the directory where the training data will be stored.
        valid_dir_name (str): The name of the directory where the validation data will be stored.
        split_ratio (float): The ratio of data to be used for training.
        random_split (bool): Whether to split the data randomly or sequentially.
        seed (int): The seed for random splitting.

    Returns:
        None
    """

    # Mendapatkan nama fungsi secara dinamis
    function_name = inspect.currentframe().f_code.co_name
    
    # Mendapatkan nama file yang berisi fungsi ini
    file_name_function = inspect.getfile(inspect.currentframe())

    print(f'\nRunning {function_name} di file {file_name_function}...')

    # Path ke file JSON COCO
    coco_json_path = glob.glob(os.path.join(project_path, '**', coco_json_filename), recursive=True)[0]

    # Path ke folder output train dan valid
    train_dir = os.path.join(project_path, train_dir_name)
    valid_dir = os.path.join(project_path, valid_dir_name)

    if os.path.exists(train_dir) or os.path.exists(valid_dir):
        print(f"\tFolder:\n \t\t1. {Path(train_dir).parent} \n \t\t2. {Path(valid_dir).parent} \n\tsudah dibuat. Hapus folder tersebut jika ingin memulai ulang.\n\n")
        return

    # Buat folder train dan valid jika belum ada
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)

    # Load file JSON COCO
    with open(coco_json_path, 'r') as file:
        coco_data = json.load(file)

    # Dapatkan daftar gambar
    images = coco_data['images']

    # Membagi dataset menjadi train dan valid
    if random_split:
        random.seed(seed)
        random.shuffle(images)  # Splitting secara acak
    split_index = int(len(images) * split_ratio)

    train_images = images[:split_index]
    valid_images = images[split_index:]

    # Buat lookup image_id untuk mempercepat pencarian anotasi terkait
    train_image_ids = set(image['id'] for image in train_images)
    valid_image_ids = set(image['id'] for image in valid_images)

    # Filter anotasi berdasarkan image_id
    train_annotations = [ann for ann in coco_data['annotations'] if ann['image_id'] in train_image_ids]
    valid_annotations = [ann for ann in coco_data['annotations'] if ann['image_id'] in valid_image_ids]

    # Salin gambar ke folder train dan valid
    for image in tqdm(train_images, desc="Copying train images"):
        src_image_path = os.path.join(project_path, 'annotations', image['file_name'])
        dest_image_path = os.path.join(train_dir, image['file_name'])
        shutil.copyfile(src_image_path, dest_image_path)

    for image in tqdm(valid_images, desc="Copying valid images"):
        src_image_path = os.path.join(project_path, 'annotations', image['file_name'])
        dest_image_path = os.path.join(valid_dir, image['file_name'])
        shutil.copyfile(src_image_path, dest_image_path)

    # Buat file JSON baru untuk train dan valid
    train_data = {
        'licenses': coco_data['licenses'],
        'info': coco_data['info'],
        'categories': coco_data['categories'],
        'images': train_images,
        'annotations': train_annotations
    }

    valid_data = {
        'licenses': coco_data['licenses'],
        'info': coco_data['info'],
        'categories': coco_data['categories'],
        'images': valid_images,
        'annotations': valid_annotations
    }

    # Simpan file JSON train dan valid
    train_json_path = os.path.join(train_dir, '_train_instances_default.json')
    valid_json_path = os.path.join(valid_dir, '_valid_instances_default.json')

    with open(train_json_path, 'w') as f:
        json.dump(train_data, f, indent=4)

    with open(valid_json_path, 'w') as f:
        json.dump(valid_data, f, indent=4)

    print(f"\tSplitting selesai. Data train: {len(train_images)} gambar, Data valid: {len(valid_images)} gambar.\n\n")