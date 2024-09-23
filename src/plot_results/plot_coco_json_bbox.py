from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import json


def coco_json_plot_image_and_bbox(json_path, base_dir, image_index=0):
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Cari annotations yang sesuai dengan image_id
    annotations_for_target = [ann for ann in data['annotations'] if ann['image_id'] == image_index]

    if len(annotations_for_target) > 0:
        # Ambil path gambar dari image_id
        image_data = next(img for img in data['images'] if img['id'] == image_index)
        img_path = os.path.join(base_dir, image_data['file_name'])  # Path ke file gambar

        # Load gambar
        img = Image.open(img_path)
        fig, ax = plt.subplots(1)
        ax.imshow(img)

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
        print(f"No annotations found for image_id {image_index}")