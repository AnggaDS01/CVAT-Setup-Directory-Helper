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
IMAGES_DIRNAME = 'train'
COCO_JSON_PATH = glob.glob(os.path.join(PROJECT_PATH, '**', COCO_JSON_FILENAME), recursive=True)[0]
IMAGES_DIR = os.path.join(PROJECT_PATH, IMAGES_DIRNAME)

image_index = random.randint(0, 300)
print(image_index)
coco_json_plot_image_and_bbox(COCO_JSON_PATH, IMAGES_DIR, image_index)