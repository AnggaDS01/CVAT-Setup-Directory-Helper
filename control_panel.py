from pathlib import Path

IMAGE_SIZE = (640, 640) # (w, h), If set to None then it will follow the original size
FPS = 5 # frame per second
EXT = 'jpg' # image extension
SPLIT_RATIO = (0.7, 0.2) # (train, val) if the total ratio of train and valid is not equal to 1.0 then the remainder will be assigned to the test ratio, and If set to None then no split will be performed
RANDOM_SPLIT = True # If set to True then it will perform random split
SEED = 42 # random seed

# ====== PATH AREA ======
VIDEO_TARGET_NAME_PATH = Path(f"Data Zone/Videos-Assets/Highway-Traffic/HT_00001/4K Video of Highway Traffic! (online-video-cutter.com).mp4") # video path
IMAGES_TARGET_DIR_PATH = Path(f"Data Zone/Annotated-Images-Assets/Highway-Traffic-02") # image directory path

# # ====== PLOT RESULT ======
# PARENT_DIR_NAME = 'valid'
# IMAGE_NAME = 'pothole_8.jpg'
# CLASS_ID_TO_NAME = {
#     0: "pothole",
#     # Tambahin sesuai label di dataset
# } # sesuaikan yang di data.yaml