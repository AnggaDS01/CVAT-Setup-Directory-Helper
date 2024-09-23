from src.plot_results.plot_pascal_voc_bbox import pascal_voc_plot_image_and_bbox
import os
import glob

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Traffic Assets' # Change this
PROJECT_NAME = 'traffic-pascalVOC' # Change this
BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
IMAGE_NAME = 'frame_000240'

pascal_voc_plot_image_and_bbox(PROJECT_PATH, IMAGE_NAME)