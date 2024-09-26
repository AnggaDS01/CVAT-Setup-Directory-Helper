import xml.etree.ElementTree as ET

def modify_xml_file(xml_path, new_extension):
    # Parse XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Temukan elemen <filename> dan ubah ekstensinya
    filename_element = root.find('filename')
    if filename_element is not None:
        # Split filename and replace the extension
        filename = filename_element.text
        base_name = filename.rsplit('.', 1)[0]  # Menghapus ekstensi lama
        current_ext = filename.rsplit('.', 1)[1]

        if current_ext.lower() == new_extension.lower():
            return False  # Tidak perlu modifikasi, ekstensi sudah benar

        new_filename = f"{base_name}.{new_extension}"  # Menambahkan ekstensi baru
        filename_element.text = new_filename  # Update nilai filename

    # Simpan perubahan kembali ke file XML
    tree.write(xml_path)
    return True