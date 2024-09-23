from src.plot_results.plot_pascal_voc_bbox import pascal_voc_plot_image_and_bbox
import os
import glob

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Traffic Assets' # Change this
PROJECT_NAME = 'traffic-pascalVOC' # Change this
BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
IMAGE_NAME = 'frame_000000'

xml_path = glob.glob(os.path.join(PROJECT_PATH, '**', IMAGE_NAME + '.xml'), recursive=True)[0]
image_path = glob.glob(os.path.join(PROJECT_PATH, '**', IMAGE_NAME + '.jpg'), recursive=True)[0]
pascal_voc_plot_image_and_bbox(xml_path, image_path)