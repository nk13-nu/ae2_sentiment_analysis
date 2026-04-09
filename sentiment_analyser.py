"""Implement the Sentiment Analysis Class here using HuggingFace's pipeline 
and through the "text-classification" model accessed on "transformersbook/distilbert-base-uncased-finetuned-emotion"""

from transformers import pipeline

sentiment_pipeline = pipeline("text-classification",model="transformersbook/distilbert-base-uncased-finetuned-emotion")

class SentimentAnalyser:
    def __init__(self, text:str):
        if not isinstance(text, str):
            raise TypeError(f"{text} must be a String")
        self.text = text

    def get_sentiment(self):
        emotion_predictions = sentiment_pipeline(self.text, top_k=None)
        
        return {
            "text": self.text,
            "labels": emotion_predictions
        }
