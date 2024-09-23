from src.plot_results.plot_yolo_bbox import yolo_plot_image_and_bbox
import os
import glob

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Traffic Assets' # Change this
PROJECT_NAME = 'traffic-YOLOv8' # Change this
BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
IMAGE_NAME = 'frame_000000'

class_id_to_name = {
    0: "car",
    # Tambahin sesuai label di dataset lo
}

txt_path = glob.glob(os.path.join(PROJECT_PATH, '**', IMAGE_NAME + '.txt'), recursive=True)[0]
image_path = glob.glob(os.path.join(PROJECT_PATH, '**', IMAGE_NAME + '.jpg'), recursive=True)[0]

# Plot gambar dan bounding box
yolo_plot_image_and_bbox(txt_path, image_path, class_id_to_name)