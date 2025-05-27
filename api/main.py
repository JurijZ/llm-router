from fastapi import FastAPI
from pydantic import BaseModel
from recommender import Recommender, Recommendation
from llm_classifier import ContentComplexity, LLMClassifier

app = FastAPI()
llm_classfier = LLMClassifier()
recommender = Recommender()

class Prompt(BaseModel):
    text: str

class Classification(BaseModel):
    complexity: ContentComplexity
    recommendation: Recommendation

@app.post("/classify", response_model=Classification)
async def classify_prompt(prompt: Prompt):
    try:
        # Analyze the content using the LLM classifier
        complexity = await llm_classfier.analyze_content(prompt.text)

        # Get recommendations based on the complexity analysis
        recommendation = await recommender.get_recommendations(complexity)

        return Classification(
            complexity=complexity,
            recommendation=recommendation
        )
    
    except Exception as e:
        return {"error": str(e)}