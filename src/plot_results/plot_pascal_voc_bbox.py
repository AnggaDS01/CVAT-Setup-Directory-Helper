import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

def pascal_voc_plot_image_and_bbox(xml_path, image_path):
    # Fungsi untuk membaca XML Pascal VOC
    def parse_voc_xml(xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        objects = []
        for obj in root.findall('object'):
            # Ambil label dari tag 'name'
            label = obj.find('name').text
            
            # Ambil koordinat bounding box dari tag 'bndbox'
            bndbox = obj.find('bndbox')
            xmin = float(bndbox.find('xmin').text)
            ymin = float(bndbox.find('ymin').text)
            xmax = float(bndbox.find('xmax').text)
            ymax = float(bndbox.find('ymax').text)
            
            bbox = [xmin, ymin, xmax, ymax]
            objects.append((label, bbox))
        
        return objects

    # Parse XML untuk mendapatkan objek dan bounding box
    objects = parse_voc_xml(xml_path)

    # Load gambar
    img = Image.open(image_path)

    # Tampilkan gambar
    fig, ax = plt.subplots(1)
    ax.imshow(img)

    # Loop melalui objek dan gambar bounding box serta labelnya
    for label, bbox in objects:
        xmin, ymin, xmax, ymax = bbox
        
        # Gambar bounding box
        rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        # Tambahkan teks di atas bounding box
        plt.text(xmin, ymin - 10, label, color='white', fontsize=10, backgroundcolor='red')

    plt.show()