# Penggunaan pipeline
from pipeline.yolo_video_to_sequence_pipeline import yolo_process_video_pipeline
from pipeline.xml_video_to_sequence_pipeline import xml_process_video_pipeline
from pipeline.json_video_to_sequence_pipeline import json_process_video_pipeline
import os

GRANDPARENT_NAME = 'Data Zone' # Put your data in this folder
PARENT_NAME = 'Traffic Assets' # Change this
PROJECT_NAME = 'traffic-COCO' # Change this
VIDEO_NAME = '4K Video of Highway Traffic! (online-video-cutter.com).mp4' # Change this
# FILE_NAMES = 'train.txt'

BASE_DIR = os.path.join(GRANDPARENT_NAME, PARENT_NAME)
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
VIDEO_PATH = os.path.join(BASE_DIR, VIDEO_NAME)

# yolo_process_video_pipeline(PROJECT_PATH, VIDEO_PATH, FILE_NAMES, PROJECT_NAME)
# xml_process_video_pipeline(PROJECT_PATH, VIDEO_PATH, FILE_NAMES)
json_process_video_pipeline(PROJECT_PATH, VIDEO_PATH)