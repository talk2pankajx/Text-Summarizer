from Text_Summarizer.constants import *
from Text_Summarizer.logging import logger
from Text_Summarizer.utils.common import read_yaml_file, create_directories
import os
from Text_Summarizer.entity import (DataIngestionConfig,
                                    DataValidationConfig)

class ConfigurationManager:
    def __init__(self, config_file_path = CONFIG_PATH,
                 params_file_path = PARAMS_PATH):
        self.config = read_yaml_file(config_file_path)
        self.params = read_yaml_file(params_file_path)
        
        create_directories([self.config.artifacts_root])
    

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
        root_dir=config.root_dir,
        source_url=config.source_url,
        local_data_file=config.local_data_file,
        unzip_dir=config.unzip_dir,
    
        
    )
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        
        config = self.config.data_validation
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )
        
        return data_validation_config
    
