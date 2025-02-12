from Text_Summarizer.config.configuration import ConfigurationManager
from Text_Summarizer.components.model_training import ModelTrainer
from Text_Summarizer.logging import logger


class ModelTrainingPipeline:
    def __init__(self,):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=data_transformation_config)
        model_trainer_config.train()
