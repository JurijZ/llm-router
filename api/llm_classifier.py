# Based on Bloom's Taxonomy
import os
import openai
from pydantic import BaseModel, Field

class ContentComplexity(BaseModel):
    remembering_complexity: int = Field(..., ge=1, le=10, description="Requires recalling or finding facts (1-10)")
    creation_complexity: int = Field(..., ge=1, le=10, description="Requires to formulate new theories, design solutions (1-10)")
    evaluation_complexity: int = Field(..., ge=1, le=10, description="Requires to make and defend judgments (1-10)")
    analysis_complexity: int = Field(..., ge=1, le=10, description="Requires breaking down information and seeing relationships (1-10)")
    synthesis_complexity: int = Field(..., ge=1, le=10, description="Requires information integration from multiple sources, disciplines, or concepts (1-10)")
    applying_complexity: int = Field(..., ge=1, le=10, description="Requires to use knowledge in a new situation (1-10)")
    hypothesis_complexity: int = Field(..., ge=1, le=10, description="Requires hypothetical thinking (1-10)")

class LLMClassifier():
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    async def analyze_content(self, user_question: str) -> ContentComplexity:
    
        system_prompt = """
    You are an expert content evaluator. Given the following content, evaluate it based on the provided criteria and return a JSON object with integer scores (1-10) for each property. 
    Ensure all values are integers between 1 and 10.

    Criteria:
    - remembering_complexity: Requires recalling or finding facts (1=simple, 10=complex).
    - creation_complexity: Requires to formulate new theories, design solutions (1=simple, 10=complex).
    - evaluation_complexity: Requires to make and defend judgments (1=simple, 10=complex).
    - analysis_complexity: Requires breaking down information and seeing relationships (1=simple, 10=complex).
    - synthesis_complexity: Requires information integration from multiple sources, disciplines, or concepts (1=simple, 10=complex).
    - applying_complexity: Requires to use knowledge in a new situation (1=simple, 10=complex).
    - hypothesis_complexity: Requires hypothetical thinking (1=simple, 10=complex).

    Return a JSON object with these fields and integer values between 1 and 10.
    """

        try:
            response = await self.client.beta.chat.completions.parse(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Analyze this content: {user_question}"}
                ],
                response_format=ContentComplexity,
                temperature=0.1
            )
            
            return response.choices[0].message.parsed
        
        except Exception as e:
            print(f"Error analyzing question: {e}")
            return None

