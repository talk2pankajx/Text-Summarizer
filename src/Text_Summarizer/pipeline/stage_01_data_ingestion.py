
from Text_Summarizer.config.configuration import ConfigurationManager
from Text_Summarizer.components.data_ingestion import DataIngestion
from Text_Summarizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self,):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.unzip_data()
        except Exception as e:
            raise e
