import yaml

# Fungsi untuk membaca class dari file data.yaml yang sudah ada
def extract_classes_from_data_yaml(data_yaml_path):
    '''
    Extracts class names from a YOLO data.yaml file.

    Parameters:
        data_yaml_path (str): The path to the data.yaml file.

    Returns:
        list: A list of class names. If 'names' in data.yaml is a dictionary, 
            returns a list of its values; otherwise, returns the 'names' list directly.

    Raises:
        ValueError: If 'names' is not found in the data.yaml file.
    '''

    # Baca file data.yaml
    with open(data_yaml_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

        # Ambil nama kelas dari data.yaml
        if 'names' in data:
            if isinstance(data['names'], dict):
                return list(data['names'].values())  # Ambil nama kelas dari dict names
            else:
                return data['names']
        else:
            raise ValueError("Bagian 'names' tidak ditemukan di file data.yaml.")