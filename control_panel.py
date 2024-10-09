import os

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Traffic Assets' # Change this
PROJECT_NAME = 'traffic-YOLOv8' # Change this
FILE_NAMES = 'train.txt'
SPLIT_RATIO = 0.8
RANDOM_SPLIT = True
IS_SPLIT = True
SEED = 42
EXT = 'jpg'

# ====== PATH AREA ======
BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
VIDEO_NAME = '4K Video of Highway Traffic! (online-video-cutter.com).mp4' # Change this
VIDEO_PATH = os.path.join(BASE_DIR, VIDEO_NAME)

# ====== PLOT RESULT ======
PARENT_DIR_NAME = 'train'
IMAGE_NAME = 'frame_000391.jpg'
CLASS_ID_TO_NAME = {
    0: "car",
    # Tambahin sesuai label di dataset
} # sesuaikan yang di data.yaml