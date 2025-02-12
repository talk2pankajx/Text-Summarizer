
from Text_Summarizer.config.configuration import ConfigurationManager
from Text_Summarizer.components.data_transformation import DataTransformation
from Text_Summarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e
