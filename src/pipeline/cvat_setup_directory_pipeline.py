from src.pipeline.yolo_pipeline import yolo_pipeline_format_processor
from src.pipeline.coco_pipeline import coco_pipeline_format_processor
from src.pipeline.pacal_voc_pipeline import pascal_voc_pipeline_format_processor
from pathlib import Path


def setup_dir_pipeline(
    format_output=None,
    source_path: Path=None, 
    fps: int=30, 
    images_ext: str='jpg', 
    image_size: tuple=None, 
    split_ratio=None, 
    random_split: bool=True,
    seed: int=42, 
) -> None:

    """
    Sets up the directory pipeline based on the specified output format.

    This function processes the source path and its content according to the chosen format
    for object detection datasets. It supports three formats: 'yolo', 'coco', and 'pascal_voc'.
    Depending on the format, it extracts frames from videos, sets up the directory structure,
    and optionally splits the dataset into training, validation, and test sets.

    Parameters:
        format_output (str): The desired output format for the dataset ('yolo', 'coco', 'pascal_voc').
        source_path (Path): The path to the source directory containing videos or images.
        fps (int): Frames per second to extract from videos.
        images_ext (str): The file extension for images.
        image_size (tuple): The desired size for the output images.
        split_ratio (tuple): The ratio for splitting the dataset (e.g., (0.8, 0.1) for train and validation).
        random_split (bool): Whether to randomly split the dataset.
        seed (int): Seed for random splitting.

    Returns:
        None
    """

    match format_output:
        case 'yolo':
            yolo_pipeline_format_processor(
                source_path=source_path, 
                fps=fps,
                images_ext=images_ext, 
                image_size=image_size, 
                split_ratio=split_ratio, 
                random_split=random_split,
                seed=seed, 
            )

        case 'coco':
            coco_pipeline_format_processor(
                source_path=source_path, 
                fps=fps, 
                images_ext=images_ext, 
                image_size=image_size, 
                split_ratio=split_ratio, 
                random_split=random_split,
                seed=seed, 
            )

        case 'pascal_voc':
            pascal_voc_pipeline_format_processor(
                source_path=source_path, 
                fps=fps, 
                images_ext=images_ext, 
                image_size=image_size, 
                split_ratio=split_ratio, 
                random_split=random_split,
                seed=seed, 
            )

        case _:
            raise ValueError(f"Unsupported output format: {format_output}\nSupported formats: 'yolo', 'coco', 'pascal_voc'")

    return 