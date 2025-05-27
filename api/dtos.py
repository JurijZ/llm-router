from enum import Enum
from typing import Optional

from pydantic import BaseModel

from llm_classifier import ContentComplexity


class GradationValues(str, Enum):
    HIGH = "high"
    LOW = "low"

class PromptParameters(BaseModel):
    cost: GradationValues = GradationValues.LOW
    speed: GradationValues = GradationValues.HIGH

class Prompt(BaseModel):
    text: str = "What is the capital of Lithuania?"
    prompt_parameters: Optional[PromptParameters] = None

class Recommendation(BaseModel):
    recommended_model: str = "gpt-4.1-mini"
    prompt_complexity: str = "average"

class Classification(BaseModel):
    complexity: ContentComplexity
    recommendation: Recommendation