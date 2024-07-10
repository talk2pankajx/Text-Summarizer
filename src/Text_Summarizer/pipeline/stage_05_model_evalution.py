from Text_Summarizer.config.configuration import  ConfigurationManager

from Text_Summarizer.components.model_evaluation import ModelEvaluation


class ModelEvalutionTrainingPipeline:
    def __init__(self,):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            score = model_evaluation.evaluate()
            return score
        except Exception as e:
            raise e