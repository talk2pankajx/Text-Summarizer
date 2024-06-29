import os
from Text_Summarizer.constants import *
from Text_Summarizer.logging import logger
import zipfile
import urllib.request as request
import os
from Text_Summarizer.utils.common import get_size
from Text_Summarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url= self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} dowloaded the following info: \n{headers}")
        else:
            logger.info(f"file already exists of size{get_size(Path(self.config.local_data_file))}")   
            
            
    def unzip_data(self):
        
        unzip_path  = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
