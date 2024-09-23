import json

json_path = 'port/annotations/person_keypoints_default.json'

with open(json_path, 'r') as file:
    data = json.load(file)

with open(json_path, 'w') as f:
    json.dump(data, f, indent=4)