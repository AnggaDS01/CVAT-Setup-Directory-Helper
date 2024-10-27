# import os
# import json

# base_dir = 'Data Zone/Traffic Assets/traffic-COCO'

# annotations_json = 'annotations/_instances_default.json'
# train_json = 'train/_train_instances_default.json'
# valid_json = 'valid/_valid_instances_default.json'

# json_path = os.path.join(base_dir, annotations_json) 
# train_json_path = os.path.join(base_dir, train_json) 
# valid_json_path = os.path.join(base_dir, valid_json) 

# with open(json_path, 'r') as file:
#     coco_data = json.load(file)

# with open(train_json_path, 'r') as file:
#     train_coco_data = json.load(file)
    
# with open(valid_json_path, 'r') as file:
#     valid_coco_data = json.load(file)

# print('\n\n')
# print(coco_data.keys())
# print(train_coco_data.keys())
# print(valid_coco_data.keys())
# print('\n\n')

# images = []
# train_images = []
# valid_images = []

# for i in range(len(coco_data['images'])):
#     images.append(coco_data['images'][i]['file_name'])

# for i in range(len(train_coco_data['images'])):
#     train_images.append(train_coco_data['images'][i]['file_name'])

# for i in range(len(valid_coco_data['images'])):
#     valid_images.append(valid_coco_data['images'][i]['file_name'])

# valid_images_list = os.listdir(os.path.join(base_dir, 'valid'))[:-1]
# train_images_list = os.listdir(os.path.join(base_dir, 'train'))[:-1]

# print(sorted(valid_images) == sorted(valid_images_list))
# print(sorted(train_images) == sorted(train_images_list))
# print(coco_data['categories'] == train_coco_data['categories'])
# print(coco_data['categories'] == valid_coco_data['categories'])

# print('\n\n')

import globox
import json
from pathlib import Path

def main() -> None:
    txt_path = Path("Data Zone/Annotated-Images-Assets/Highway-Traffic/HT_00001/data_train/labels/")  # Where the .txt files are
    images_path = Path("Data Zone/Annotated-Images-Assets/Highway-Traffic/HT_00001/data_train/images/")  
    save_file = Path("Data Zone/")

    # YOLOv5
    yolo = globox.AnnotationSet.from_yolo_v5(
        folder=txt_path,
        image_folder=images_path
    )

    # yolo.save_coco(save_file, auto_ids=True)

    yolo.save_pascal_voc(save_file)

    # with open(save_file, 'r') as file:
    #     data = json.load(file)

    # with open(save_file, 'w') as f:
    #     json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()