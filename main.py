from Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Text_Summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Text_Summarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from Text_Summarizer.pipeline.stage_05_model_evalution import ModelEvalutionTrainingPipeline
from Text_Summarizer.logging import logger


STAGE_NAME = 'data_ingestion_stage'

try:
    logger.info("stating data ingestion training pipeline")
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.info("data ingestion training pipeline completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'data_validation_stage'

try:
    logger.info("stating data validation stage pipeline")
    data_validation_training_pipeline = DataValidationTrainingPipeline()
    data_validation_training_pipeline.main()
    logger.info("data validation stage pipeline completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'data_transformation_stage'

try:
    logger.info("stating data transformation stage pipeline")
    data_transformation_training_pipeline = DataTransformationTrainingPipeline()
    data_transformation_training_pipeline.main()
    logger.info("data transformation stage pipeline completed")
except Exception as e:
    logger.exception(e)
    raise e

    
STAGE_NAME = 'model_trainer_stage'

try:
    logger.info("stating model training stage pipeline")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info("model training pipeline completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'model_evalution_stage'

try:
    logger.info("stating model evalution stage pipeline")
    model_evaluation_pipeline = ModelEvalutionTrainingPipeline()
    model_evaluation_pipeline.main()
    logger.info("model evaluation pipeline completed")
except Exception as e:
    logger.exception(e)
    raise e