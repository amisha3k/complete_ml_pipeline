import os
import yaml
import logging
import json
import joblib
from box import ConfigBox  # access YAML keys as attributes
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any, List

# Optional: configure a simple logger
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(message)s]",
    handlers=[logging.StreamHandler()]
)

def read_yaml(path: Path) -> ConfigBox:
    """
    Read a YAML file and return its content as a ConfigBox.
    """
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"YAML file loaded successfully: {path}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"YAML file is empty: {path}")
    except Exception as e:
        raise e

def create_directories(paths: List[Path], verbose: bool = True):
    """
    Create directories if they don't exist.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Directory created or already exists: {path}")

def save_json(path: Path, data: dict):
    """
    Save a dictionary to a JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logging.info(f"JSON file saved at: {path}")

def load_json(path: Path) -> ConfigBox:
    """
    Load a JSON file and return as ConfigBox.
    """
    with open(path) as f:
        content = json.load(f)
        return ConfigBox(content)

def save_bin(data: Any, path: Path):
    """
    Save any Python object as a binary file using joblib.
    """
    joblib.dump(data, path)
    logging.info(f"Binary file saved at: {path}")

def load_bin(path: Path) -> Any:
    """
    Load a binary file using joblib.
    """
    return joblib.load(path)

# import os
# import yaml
# import logging
# from  src.datascience import logger
# import json
# import joblib
# from ensure import ensure_annotations #type casting
# from box import ConfigBox #to access the keys in dictionary in yaml
# from pathlib import Path
# from typing import Any
# from box.exceptions import BoxValueError

# @ensure_annotations
# def read_yaml(path: Path) -> ConfigBox:
#     try:
#         with open(path) as yaml_file:
#             content = yaml.safe_load(yaml_file)
#             logging.info(f"YAML file: {path} loaded successfully")
#             return ConfigBox(content)
#     except BoxValueError:
#         raise ValueError("YAML file is empty")
#     except Exception as e:
#         raise e

# @ensure_annotations
# def create_directories(paths: List[Path], verbose: bool = True):
#     for path in paths:
#         os.makedirs(path, exist_ok=True)
#         if verbose:
#             print(f"Created directory at: {path}")

# def save_json(path: Path, data: dict):
#     with open(path, "w") as f:
#         json.dump(data, f, indent=4)

# def load_json(path: Path) -> ConfigBox:
#     with open(path) as f:
#         content = json.load(f)
#         return ConfigBox(content)

# def save_bin(data: Any, path: Path):
#     joblib.dump(data, path)
#     print(f"Binary file saved at: {path}")

# def load_bin(path: Path) -> Any:
#     return joblib.load(path)

