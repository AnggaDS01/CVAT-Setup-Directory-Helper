import os

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Potholes-Assets' # Change this
PROJECT_NAME = 'potholes-YOLOv8' # Change this
FILE_NAMES = 'train.txt'
SPLIT_RATIO = 0.8
RANDOM_SPLIT = True
IS_SPLIT = True
IS_VIDEO_PATH = False
SEED = 42
EXT = 'jpg'

# ====== PATH AREA ======
BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
VIDEO_NAME = '' # Change this
VIDEO_PATH = os.path.join(BASE_DIR, VIDEO_NAME)

# ====== PLOT RESULT ======
PARENT_DIR_NAME = 'annotations'
IMAGE_NAME = 'pothole_4.jpg'
CLASS_ID_TO_NAME = {
    0: "pothole",
    # Tambahin sesuai label di dataset
} # sesuaikan yang di data.yaml