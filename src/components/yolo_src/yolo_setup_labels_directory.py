from src.constants import *
import os

def yolo_setup_labels_dir(output_labels_dir, output_images_dir) -> None:
    """
    Sets up the directory structure for YOLO labels.

    This function creates the directory for labels if it does not exist, and if the directory is empty, it loops through all files in the images directory and creates an empty .txt file for each one.

    Parameters:
        output_labels_dir (Path): The path to the directory where the labels will be saved.
        output_images_dir (Path): The path to the directory containing the images.

    Returns:
        None
    """

    # Create the output directory for labels if it doesn't already exist
    if not os.path.exists(output_labels_dir):
        os.makedirs(output_labels_dir, exist_ok=True)
        print(f"\t[INFO] The directory '{output_labels_dir}' was created successfully.")
    else:
        print(f"\t[INFO] The directory '{output_labels_dir}' already exists.")
    
    # Check if the labels directory is empty; if not, skip label file creation
    if os.listdir(output_labels_dir):
        print(f"\t\t[INFO] The directory '{output_labels_dir}' is not empty. Skipping...")
    else:
        # For each image file in the output images directory, create an empty label file
        for filename in os.listdir(output_images_dir):
            if IMAGE_EXTENSIONS_PATTERN.search(filename):  # Process only files with matching image extensions
                # Define the name and path for the corresponding label file
                txt_filename = os.path.splitext(filename)[0] + '.txt'
                txt_file_path = os.path.join(output_labels_dir, txt_filename)
                
                # Create an empty label file
                open(txt_file_path, 'w').close() 
                
        print(f"\t\t[INFO] Label files created for images in '{output_images_dir}'.")

    return 