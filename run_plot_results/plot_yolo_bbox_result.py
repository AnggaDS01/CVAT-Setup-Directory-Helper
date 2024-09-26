from src.components.plot_results.plot_yolo_bbox import yolo_plot_image_and_bbox
from src.constants import *

yolo_plot_image_and_bbox(
    PROJECT_PATH, 
    PARENT_DIR_NAME, 
    IMAGE_NAME, 
    CLASS_ID_TO_NAME
)