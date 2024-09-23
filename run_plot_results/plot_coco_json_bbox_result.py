from src.plot_results.plot_coco_json_bbox import coco_json_plot_image_and_bbox

import glob
import random
import os

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Traffic Assets' # Change this
PROJECT_NAME = 'traffic-COCO' # Change this
BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
COCO_JSON_FILENAME = '_instances_default.json'

image_index = random.randint(200, 300)
coco_json_plot_image_and_bbox(PROJECT_PATH, COCO_JSON_FILENAME, image_index=390)