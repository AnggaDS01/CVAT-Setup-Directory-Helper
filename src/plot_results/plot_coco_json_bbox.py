from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import json

def coco_json_plot_image_and_bbox(json_path, base_dir, image_index=0):
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Map antara ID gambar dengan path file gambar
    image_id_to_file = {image['id']: image['file_name'] for image in data['images']}

    # Map antara category_id dengan nama kategorinya
    category_id_to_name = {category['id']: category['name'] for category in data['categories']}

    # Pilih gambar yang ingin ditampilkan (bisa berdasarkan image_id)
    image_id = data['annotations'][image_index]['image_id']  # contoh: ambil image_id dari annotation pertama
    img_path = os.path.join(base_dir, image_id_to_file[image_id])
    img = Image.open(img_path)

    # Tampilkan gambar
    fig, ax = plt.subplots(1)
    ax.imshow(img)

    # Loop semua annotations yang berkaitan dengan image_id ini
    for annotation in data['annotations']:
        if annotation['image_id'] == image_id:
            bbox = annotation['bbox']  # Format: [x_min, y_min, width, height]
            category_id = annotation['category_id']  # Ambil kategori objek
            category_name = category_id_to_name[category_id]  # Cari nama kategori

            # Gambar bounding box
            x_min, y_min, width, height = bbox
            rect = patches.Rectangle((x_min, y_min), width, height, linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

            # Tambahkan teks di atas bounding box
            plt.text(x_min, y_min - 10, category_name, color='white', fontsize=12, backgroundcolor='red')

    plt.show()