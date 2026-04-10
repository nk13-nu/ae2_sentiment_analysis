"""
Define Data Models using Pydantic's BaseModel here
"""

from pydantic import BaseModel

class EmotionScoring(BaseModel):
    label: str
    score: float

class APIResponse(BaseModel):
    text: str
    labels: list[EmotionScoring]

class TextSubmitted(BaseModel):
    customer_review: str
