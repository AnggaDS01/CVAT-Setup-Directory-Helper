from src.plot_results.plot_yolo_bbox import yolo_plot_image_and_bbox
import os
import glob

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Traffic Assets' # Change this
PROJECT_NAME = 'traffic-YOLOv8' # Change this
BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
IMAGE_NAME = 'frame_000322'

class_id_to_name = {
    0: "car",
    # Tambahin sesuai label di dataset
} # sesuai yang di data.yaml

# Plot gambar dan bounding box
yolo_plot_image_and_bbox(PROJECT_PATH, IMAGE_NAME, class_id_to_name)