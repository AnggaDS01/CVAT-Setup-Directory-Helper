from pathlib import Path

IMAGE_SIZE = None
FPS = 3
EXT = 'jpg'
SPLIT_RATIO = (0.7, 0.2)
RANDOM_SPLIT = True
SEED = 42

# ====== PATH AREA ======
VIDEO_TARGET_NAME_PATH = Path(f"Data Zone/Videos-Assets/Highway-Traffic/HT_00001/4K Video of Highway Traffic! (online-video-cutter.com).mp4")
IMAGES_TARGET_DIR_PATH = Path(f"C:/Workspace/Python Area/CVAT-Setup-Directory-Helper/Data Zone/Annotated-Images-Assets/aaq")

# # ====== PLOT RESULT ======
# PARENT_DIR_NAME = 'valid'
# IMAGE_NAME = 'pothole_8.jpg'
# CLASS_ID_TO_NAME = {
#     0: "pothole",
#     # Tambahin sesuai label di dataset
# } # sesuaikan yang di data.yaml