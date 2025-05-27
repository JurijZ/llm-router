from fastapi import FastAPI
from dtos import Classification, Prompt
from recommender import Recommender
from llm_classifier import LLMClassifier

app = FastAPI()
llm_classfier = LLMClassifier()
recommender = Recommender()


@app.post("/classify", response_model=Classification)
async def classify_prompt(prompt: Prompt):
    try:
        # Analyze the prompt using the LLM classifier
        complexity = await llm_classfier.analyze_content(prompt.text)

        # Get recommendations based on the complexity analysis
        recommendation = await recommender.get_recommendations(complexity, prompt.prompt_parameters)

        return Classification(
            complexity=complexity,
            recommendation=recommendation
        )
    
    except Exception as e:
        return {"error": str(e)}