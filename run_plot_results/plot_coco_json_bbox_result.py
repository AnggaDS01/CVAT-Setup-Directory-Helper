from src.components.plot_results.plot_coco_json_bbox import coco_json_plot_image_and_bbox

import glob
import random
import os

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Traffic Assets' # Change this
PROJECT_NAME = 'traffic-COCO' # Change this
BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
COCO_JSON_FILENAME = '_valid_instances_default.json'
TARGET_IMAGE_NAME = 'frame_000005.jpg'

coco_json_plot_image_and_bbox(PROJECT_PATH, COCO_JSON_FILENAME, TARGET_IMAGE_NAME)