import yaml

# Fungsi untuk membaca class dari file data.yaml yang sudah ada
def extract_classes_from_data_yaml(data_yaml_path):

    with open(data_yaml_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        if 'names' in data:
            if isinstance(data['names'], dict):
                return list(data['names'].values())  # Ambil nama kelas dari dict names
            else:
                return data['names']
        else:
            raise ValueError("Bagian 'names' tidak ditemukan di file data.yaml.")