from Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.logging import logger


STAGE_NAME = 'data_ingestion_training'

try:
    logger.info("stating data ingestion training pipeline")
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.info("data ingestion training pipeline completed")
except Exception as e:
    logger.exception(e)
    raise e


    
