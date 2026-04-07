"""
In this script we should define the non-persistent storage class - an object that
stores the responses made to the current server which has a method to calculate
and return the average responses and is accessible from an endpoint.
"""
from typing import List, Dict

class SentimentWarehouse:
    def __init__(self, sentiments: List[Dict] = None):
        if sentiments is not None:
          self.sentiments = sentiments
        else:
            self.sentiments = []

    def store(self, sentiments):
        self.sentiments.append(sentiments)

    def get_all_sentiments(self):
        return self.sentiments
    
    def calculate_average_sentiment(self):
        pass