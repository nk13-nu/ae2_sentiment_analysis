"""
Implement the FastAPI API here, using the data models and sentiment analyser classes.
Define all endpoints and non-persistent storage.
"""
from fastapi import FastAPI
from sentiment_analyser import SentimentAnalyser
from sentiment_warehouse import SentimentWarehouse
from data_validation import APIResponse

app = FastAPI(title= "Customer Feedback Sentiment Analysis API", 
              summary="""
              This API embeds a transformer-based sentiment analysis ML model from Hugging Face to rate customer feedback
              across six emotions (sadness, joy, anger, fear, love and surprise). It includes four endpoints.""", 
              version="1.0")

sentiment_warehouse = SentimentWarehouse()

@app.get("/", tags=["Main Page"])
def root():
    return {"message": "Welcome to the Sentiment Analysis API. This API is intended for organisations to classify user feedback across six emotions and improve products and customer service."}

@app.get("/sentiment/{text}", summary="Input a product or service review and get a sentiment score across six emotions", 
         description="This endpoint takes a product review as text and returns six different scores across six emotions.", 
         response_model=APIResponse,
         tags=["Sentiment Analysis (Across Six Emotions)"])
def analyse_sentiment(text:str):
    prediction = SentimentAnalyser(text=text).get_sentiment()
    sentiment_warehouse.store(prediction)
    return prediction

@app.get("/analyse/allSentiments",
         summary="Retrieve all sentiments for each piece of text in this session.",
         tags=["Analytics"])
def all_sentiments():
    return sentiment_warehouse.get_all_sentiments()

@app.get("/analyse/averageSentiment",
         summary="Retrieve the average sentiment per emotion across all current product reviews.",
         tags=["Analytics"])
def average_sentiment():
    return sentiment_warehouse.calculate_average_sentiment()