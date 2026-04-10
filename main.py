"""
FastAPI API implementation, using the data models, sentiment analyser class and the non-persistent storage.
All endpoints are defined.
"""
from fastapi import FastAPI
from sentiment_analyser import SentimentAnalyser
from sentiment_warehouse import SentimentWarehouse
from data_validation import APIResponse, TextSubmitted

#creating the fast api object
app = FastAPI(title= "Customer Feedback Sentiment Analysis API", 
              summary="""
              This API embeds a transformer-based sentiment analysis ML model from Hugging Face to rate customer feedback
              across six emotions (sadness, joy, anger, fear, love and surprise). It includes four endpoints.""", 
              version="1.0")

#initialising the sentiment warehouse object
sentiment_warehouse = SentimentWarehouse()

#root endpoint with Main page tag
@app.get("/", tags=["Main Page"])
def root():
    return {"message": "Welcome to the Sentiment Analysis API. This API is intended for organisations to classify user feedback across six emotions and improve products and customer service."}

#post endpoint to send customer feedback that calls the analyse sentiment method to pass the text through the model, store the result non-persistently and return the result
@app.post("/sentiment", summary="Input a product or service review and get a sentiment score across six emotions", 
         description="This endpoint takes a product review as text and returns six different scores across six emotions.", 
         response_model=APIResponse,
         tags=["Sentiment Analysis (Across Six Emotions)"])
def analyse_sentiment(text: TextSubmitted):
    prediction = SentimentAnalyser(text= text.customer_review).get_sentiment()
    sentiment_warehouse.store(prediction)
    return prediction

#endpoint in within the analyse path to retrieve all sentiments from the warehouse using the get_all_sentiments method
@app.get("/analyse/allSentiments",
         summary="Retrieve all sentiments for each piece of text in this session.",
         tags=["Analytics"])
def all_sentiments():
    return sentiment_warehouse.get_all_sentiments()

#again, endpoint within analyse to calculate the average score per emotion stored in the warehouse with the calculate_average_sentiment method
@app.get("/analyse/averageSentiment",
         summary="Retrieve the average sentiment per emotion across all current product reviews.",
         tags=["Analytics"])
def average_sentiment():
    return sentiment_warehouse.calculate_average_sentiment()