from pathlib import Path

IMAGE_SIZE = None
FPS = 3
EXT = 'jpg'
SPLIT_RATIO = (0.9, 0.1) # UPDATE BAGIAN FUNGSI INI AGAR BISA BERULANG KALI DI GUNAKAN, SEHINGGA TIDAK PERLU MENGEMBALIKAN KE KEADAAN AWAL
RANDOM_SPLIT = True
SEED = 42

# ====== PATH AREA ======
VIDEO_TARGET_NAME_PATH = Path(f"Data Zone/Videos-Assets/Highway-Traffic/HT_00001/4K Video of Highway Traffic! (online-video-cutter.com).mp4")
IMAGES_TARGET_DIR_PATH = Path(f"C:/Workspace/Python Area/Computer-Vision-Annotator-Studio/Data Zone/Annotated-Images-Assets/Highway-Traffic-01/HT_00001")

# ====== PLOT RESULT ======
PARENT_DIR_NAME = 'valid'
IMAGE_NAME = 'pothole_8.jpg'
CLASS_ID_TO_NAME = {
    0: "pothole",
    # Tambahin sesuai label di dataset
} # sesuaikan yang di data.yaml