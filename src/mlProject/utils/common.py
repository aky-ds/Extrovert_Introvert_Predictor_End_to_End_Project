import os
from pathlib import Path
from typing import Any
from box import ConfigBox
from ensure import ensure_annotations
import yaml
from src.mlProject import logger
import json
import joblib 
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For any other errors encountered while reading the file.

    Returns:
        ConfigBox: Content of the YAML file wrapped in a ConfigBox.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("YAML file is empty or malformed") from e
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of paths to directories to be created.
        verbose (bool, optional): If True, logs the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> dict:
    """Loads a JSON file and returns its content as a dictionary.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        dict: Content of the JSON file.
    """
    with open(path, "r") as json_file:
        data = json.load(json_file)
        logger.info(f"JSON file loaded from: {path}")
        return data
@ensure_annotations
def save_object(file_path: Path, obj: Any):
    """Saves an object to a file using joblib.

    Args:
        file_path (Path): Path to the file where the object will be saved.
        obj (Any): The object to be saved.
    """
    joblib.dump(obj, file_path)
    logger.info(f"Object saved at: {file_path}")

@ensure_annotations
def load_object(file_path: Path) -> Any:
    """Loads an object from a file using joblib.

    Args:
        file_path (Path): Path to the file from which the object will be loaded.

    Returns:
        Any: The loaded object.
    """
    obj = joblib.load(file_path)
    logger.info(f"Object loaded from: {file_path}")
    return obj

@ensure_annotations
def get_size_of_file(file_path: Path) -> int:
    """Gets the size of a file in bytes.

    Args:
        file_path (Path): Path to the file.

    Returns:
        int: Size of the file in bytes.
    """
    size = os.path.getsize(file_path)
    logger.info(f"Size of file {file_path} is {size} bytes")
    return size