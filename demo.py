import os
import json

base_dir = 'Data Zone/Traffic Assets/traffic-COCO'

annotations_json = 'annotations/_instances_default.json'
train_json = 'train/_train_instances_default.json'
valid_json = 'valid/_valid_instances_default.json'

json_path = os.path.join(base_dir, annotations_json) 
train_json_path = os.path.join(base_dir, train_json) 
valid_json_path = os.path.join(base_dir, valid_json) 

with open(json_path, 'r') as file:
    coco_data = json.load(file)

with open(train_json_path, 'r') as file:
    train_coco_data = json.load(file)
    
with open(valid_json_path, 'r') as file:
    valid_coco_data = json.load(file)

print('\n\n')
print(coco_data.keys())
print(train_coco_data.keys())
print(valid_coco_data.keys())
print('\n\n')

images = []
train_images = []
valid_images = []

for i in range(len(coco_data['images'])):
    images.append(coco_data['images'][i]['file_name'])

for i in range(len(train_coco_data['images'])):
    train_images.append(train_coco_data['images'][i]['file_name'])

for i in range(len(valid_coco_data['images'])):
    valid_images.append(valid_coco_data['images'][i]['file_name'])

valid_images_list = os.listdir(os.path.join(base_dir, 'valid'))[:-1]
train_images_list = os.listdir(os.path.join(base_dir, 'train'))[:-1]

print(sorted(valid_images) == sorted(valid_images_list))
print(sorted(train_images) == sorted(train_images_list))
print(coco_data['categories'] == train_coco_data['categories'])
print(coco_data['categories'] == valid_coco_data['categories'])

print('\n\n')