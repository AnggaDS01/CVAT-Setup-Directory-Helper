import re

# Buat path untuk train, val (dan optional test)
TRAIN_DIR = 'data_train'
VALID_DIR = 'data_valid'
TEST_DIR = 'data_test'
IMAGES_DIR = 'images'
LABELS_DIR = 'labels'
ANNOTATED_DIR_NAME = "Annotated-Images-Assets"
VIDEOS_DIR_NAME = "Videos-Assets"
IMAGE_EXTENSIONS_PATTERN = re.compile(r"\.(jpe?g|png|bmp|tiff|gif|webp)$", re.IGNORECASE)
VIDEO_EXTENSIONS_PATTERN = re.compile(r"\.(mp4|avi|mov|mkv|flv|wmv|mpeg)$", re.IGNORECASE)
