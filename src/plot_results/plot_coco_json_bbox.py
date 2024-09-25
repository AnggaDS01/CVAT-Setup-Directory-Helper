from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import json
import glob


def coco_json_plot_image_and_bbox(project_path, coco_json_filename, target_image_name):
    coco_json_path = glob.glob(os.path.join(project_path, '**', coco_json_filename), recursive=True)[0]
    images_dir = Path(coco_json_path).parent

    with open(coco_json_path, 'r') as file:
        data = json.load(file)

    # Cari data gambar yang sesuai di COCO JSON berdasarkan file name
    image_data = next((img for img in data['images'] if img['file_name'] == target_image_name), None)

    if image_data is not None:
        target_image_id = image_data['id'] # Ambil ID gambar dari file name
        img_path = os.path.join(images_dir, image_data['file_name'])  # Path ke file gambar

        # Load gambar
        img = Image.open(img_path)
        fig, ax = plt.subplots(1)
        ax.imshow(img)

        # Cari annotations yang punya image_id sesuai
        annotations_for_target = [ann for ann in data['annotations'] if ann['image_id'] == target_image_id]

        if len(annotations_for_target) > 0:
            # Loop annotations buat gambar bounding box
            for ann in annotations_for_target:
                bbox = ann['bbox']
                xmin, ymin, width, height = bbox
                rect = patches.Rectangle((xmin, ymin), width, height, linewidth=2, edgecolor='r', facecolor='none')
                ax.add_patch(rect)

                # Tambahin label kelas di atas bounding box
                category_id = ann['category_id']
                category_name = next(cat['name'] for cat in data['categories'] if cat['id'] == category_id)
                plt.text(xmin, ymin - 10, category_name, color='white', fontsize=12, backgroundcolor='red')

            plt.title(f"{image_data['file_name']}")
            plt.show()
        else:
            print(f"No annotations found for image: {target_image_name}")
    else:
        print(f"Image {target_image_name} not found in COCO dataset.")