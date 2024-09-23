import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

def yolo_plot_image_and_bbox(txt_path, image_path, class_id_to_name):
    # Fungsi untuk membaca file YOLO
    def parse_yolo_txt(txt_file):
        objects = []
        with open(txt_file, 'r') as f:
            for line in f.readlines():
                data = line.strip().split()
                class_id = int(data[0])
                x_center = float(data[1])
                y_center = float(data[2])
                width = float(data[3])
                height = float(data[4])
                objects.append((class_id, x_center, y_center, width, height))
        return objects

    # Parse file YOLO untuk mendapatkan objek dan bounding box
    objects = parse_yolo_txt(txt_path)

    # Load gambar
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Tampilkan gambar
    fig, ax = plt.subplots(1)
    ax.imshow(img)

    # Loop melalui objek dan gambar bounding box serta labelnya
    for class_id, x_center, y_center, width, height in objects:
        # Konversi koordinat relatif ke absolut
        xmin = int((x_center - width / 2) * img_width)
        ymin = int((y_center - height / 2) * img_height)
        xmax = int((x_center + width / 2) * img_width)
        ymax = int((y_center + height / 2) * img_height)
        
        # Gambar bounding box
        rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        # Tambahkan label objek di atas bounding box
        label = class_id_to_name[class_id]
        plt.text(xmin, ymin - 10, label, color='white', fontsize=12, backgroundcolor='red')

    plt.show()
