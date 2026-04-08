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
        """
        Adds the current emotion/sentiment to the list of current sentiments
        """
        self.sentiments.append(sentiments)

    def get_all_sentiments(self):
        """
        Returns all emotion scores for each of the texts
        """
        return self.sentiments
    
    def calculate_average_sentiment(self):
        """
        Calculates the average sentiment for each of the emotions across all texts
        """
        
        score_totals = {}
        counter = {}

        for text in self.sentiments:
            for emotion_label in text['labels']:
                current_label = emotion_label['label']
                score = emotion_label['score']
                score_totals[current_label] = score_totals.get(current_label, 0) + score
                counter[current_label] = counter.get(current_label,0) + 1

        averages = {}
        for i in score_totals:
            averages[i] = score_totals[i] / counter[i]
        return averages