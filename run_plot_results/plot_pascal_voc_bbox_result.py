from src.plot_results.plot_pascal_voc_bbox import pascal_voc_plot_image_and_bbox
import os

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Traffic Assets' # Change this
PROJECT_NAME = 'traffic-Pascal-Voc' # Change this
BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
PARENT_DIR_NAME = 'valid'
IMAGE_NAME = 'frame_000003.jpg'

pascal_voc_plot_image_and_bbox(PROJECT_PATH, PARENT_DIR_NAME, IMAGE_NAME)