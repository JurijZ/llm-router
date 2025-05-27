from pydantic import BaseModel
from dtos import PromptParameters, Recommendation
from llm_classifier import ContentComplexity

class Recommender:
    def __init__(self):
        pass

    async def get_recommendations(self, complexity: ContentComplexity, prompt_parameters: PromptParameters) -> Recommendation:

        recommendation = Recommendation()

        # If any of the complexity scores is above 8, we recommend the most intelligent model:
        if any(score > 8 for score in complexity.model_dump().values()):
            recommendation.recommended_model="gpt-4.1",
            recommendation.prompt_complexity="high"
        # If all complexity scores are below 4, we recommend the most basic model:
        elif all(score < 4 for score in complexity.model_dump().values()):
            recommendation.recommended_model="gpt-4.1-nano",
            recommendation.prompt_complexity="low"
        # Else, we recommend the average model:
        else:
            recommendation.recommended_model="gpt-4.1-mini",
            recommendation.prompt_complexity="average"
        
        # Add additional recommendations based on prompt cost and speed
        if prompt_parameters.cost == "low":
            recommendation.recommended_model = "gpt-4.1-nano"

        if prompt_parameters.speed == "high":
            recommendation.recommended_model = "gpt-4.1-nano"

        return recommendation
        
