# A Recommendation class that analyses classification results and provides recommendations
from typing import List, Dict, Any

from pydantic import BaseModel
from llm_classifier import ContentComplexity

class Recommendation(BaseModel):
    recommended_model: str = "gpt-4.1-mini"
    prompt_complexity: str = "average"

class Recommender:
    def __init__(self):
        pass

    async def get_recommendations(self, complexity: ContentComplexity) -> Recommendation:

        # If any of the complexity scores is above 8, we recommend the most intelligent model:
        if any(score > 8 for score in complexity.model_dump().values()):
            return Recommendation(
                recommended_model="gpt-4.1",
                prompt_complexity="high"
            )
        # If all complexity scores are below 5, we recommend the most basic model:
        elif all(score < 5 for score in complexity.model_dump().values()):
            return Recommendation(
                recommended_model="gpt-4.1-nano",
                prompt_complexity="low"
            )
        # Else, we recommend the average model:
        else:
            return Recommendation(
                recommended_model="gpt-4.1-mini",
                prompt_complexity="average"
            )
        
