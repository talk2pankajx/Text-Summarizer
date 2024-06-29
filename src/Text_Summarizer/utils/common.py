import os
from box.exceptions import BoxValueError
import yaml
from Text_Summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml_file(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, "r") as f:
            content = yaml.safe_load(f)
            logger.info(f"Successfully read yaml file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e   
    
    
@ensure_annotations
def create_directories(path_to_dir: list,verbose= True):
    for path in path_to_dir:
        os.makedirs(path, exist_ok=True)
    if verbose:
        logger.info(f"Successfully created directories: {path_to_dir}")
        

@ensure_annotations
def get_size(path: Path) -> str:
    
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"    