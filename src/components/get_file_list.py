from pathlib import Path
import glob
import os
import itertools
from src.constants import *

# Fungsi untuk membaca nama file dari 'train.txt'
def get_first_n_files(dir_path: Path, n: int) -> list:
    """
    Get the first 'n' files in the specified directory and its subdirectories.
    
    Parameters:
    - dir_path (str): Path to the directory to search in.
    - images_ext (str, optional): File extension to search for..
    - n (int, optional): Number of files to retrieve. Default is 1.
    
    Returns:
    - List of file paths (up to 'n' files).
    """
    # Create a generator for matching files
    file_generator = (file for file in glob.iglob(os.path.join(dir_path, "**", "*.*"), recursive=True)
                      if IMAGE_EXTENSIONS_PATTERN.search(file))

    # Use islice to limit the result to 'n' files
    limited_files = list(itertools.islice(file_generator, n))
    
    return limited_files