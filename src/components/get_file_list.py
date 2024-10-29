from pathlib import Path
import glob
import os
import itertools
from src.constants import *

def get_first_n_files(dir_path: Path, n: int) -> list:
    """
    Retrieves the first 'n' image files from the specified directory path.

    This function searches recursively through the given directory path
    for files that match the defined image extensions and returns a list
    of the first 'n' such files found.

    Args:
        dir_path (Path): The path to the directory to search for image files.
        n (int): The number of image files to retrieve.

    Returns:
        list: A list containing the paths of the first 'n' image files found.
    """
    
    # Use a generator to filter files matching the image extensions pattern in the specified directory
    file_generator = (file for file in glob.iglob(os.path.join(dir_path, "**", "*.*"), recursive=True)
                      if IMAGE_EXTENSIONS_PATTERN.search(file))

    # Retrieve the first 'n' files matching the pattern
    limited_files = list(itertools.islice(file_generator, n))
    
    return limited_files