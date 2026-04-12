# Transformer-based Sentiment Analysis API
This project is a REST API for sentiment analysis which uses a transformer-based machine learning model to classify the emotional tone of input text. It is intended to be used by organisations to understand user feedback left by users.


## Design
The project is designed by following OOP principles and a modular architecture. It is composed of four main files with the `main.py` file containing the API itself. The API is built using FastAPI and contains four endpoints. The sentiment analysis ML model is constructed within the `sentiment_analyser.py` file. Non-persistent storage is defined in the `sentiment_warehouse.py` file which contains the SentimentWarehouse class that defines the object giving access to methods used to store the texts/sentiments, access all stored text/sentiments and get the average score per emotion across all texts. Finally, Pydantic data models are defined within the `data_validation.py` module. These models are used to ensure integrity and the correct return of HTTP codes. The previous three features are then imported within `main.py` and integrated into the API's endpoints.

## Available Endpoints and Example Usage
There are four exposed endpoints.

#### `GET /`
Root endpoint that returns a welcome message describing the API's purpose.

#### `POST /sentiment`
Classifies customer feedback across six emotions (sadness, joy, love, anger, fear, surprise) and stores the result.

**Successful Response (200) Example (using python requests)**

```python
import requests
response = requests.post(
    "http://localhost:8000/sentiment",
    json= {"customer_review": "I love this service!!"},
)
print(response.json())
```

```json
{
  "text": "I love this service!!",
  "labels": [
    {
      "label": "joy",
      "score": 0.6769371032714844
    },
    {
      "label": "love",
      "score": 0.2554417848587036
    },
    {
      "label": "anger",
      "score": 0.024003300815820694
    },
    {
      "label": "sadness",
      "score": 0.021363262087106705
    },
    {
      "label": "surprise",
      "score": 0.012875870801508427
    },
    {
      "label": "fear",
      "score": 0.009378588758409023
    }
  ]
}
```

#### `GET /analyse/allSentiments`
Returns every piece of customer feedback submitted to the API alongside its scores across the six emotions.

**Successful Response (200) Example (using python requests)**

For this example another text 'This is incredible!!!' was posted.
```python
import requests
response = requests.get("http://localhost:8000/analyse/allSentiments")
print(response.json())
```

```json
[
  {
    "text": "I love this service!!",
    "labels": [
      {
        "label": "joy",
        "score": 0.6769371032714844
      },
      {
        "label": "love",
        "score": 0.2554417848587036
      },
      {
        "label": "anger",
        "score": 0.024003300815820694
      },
      {
        "label": "sadness",
        "score": 0.021363262087106705
      },
      {
        "label": "surprise",
        "score": 0.012875870801508427
      },
      {
        "label": "fear",
        "score": 0.009378588758409023
      }
    ]
  },
  {
    "text": "This is incredible!!!",
    "labels": [
      {
        "label": "joy",
        "score": 0.7706387639045715
      },
      {
        "label": "surprise",
        "score": 0.1611715406179428
      },
      {
        "label": "fear",
        "score": 0.02187790907919407
      },
      {
        "label": "love",
        "score": 0.017188897356390953
      },
      {
        "label": "anger",
        "score": 0.01618657447397709
      },
      {
        "label": "sadness",
        "score": 0.01293632946908474
      }
    ]
  }
]
```

#### `GET /analyse/averageSentiment`
Returns the average score for each emotion across all stored customer reviews.

**Successful Response (200) Example (using python requests)**

```python
import requests
response = requests.get("http://localhost:8000/analyse/averageSentiment")
print(response.json())
```

```json
{
  "joy": 0.723787933588028,
  "love": 0.13631534110754728,
  "anger": 0.02009493764489889,
  "sadness": 0.017149795778095722,
  "surprise": 0.08702370570972562,
  "fear": 0.015628248918801546
}
```

## Project Structure
The project follows a modular and oop-based architecture.
```
.
├── main.py                 # FastAPI application entry point where all endpoints are defined
├── sentiment_analyser.py   # Sentiment Analysis class where the model is created by using Hugging Face's pipeline method
├── sentiment_warehouse.py  # Non-persistent text classification storage
├── data_validation.py      # Pydantic BaseModel validation following the ml response mode
├── requirements.txt        # Python dependencies required to run locally
├── README.md               # You are here
└── LICENSE                 # MIT Licence for replication
```

## Installation (using uv)
1. **Clone the repository:**
```bash
   git clone https://github.com/nk13-nu/ae2_sentiment_analysis.git
   cd ae2_sentiment_analysis
```

3. **Initialise uv:**
```bash
   uv init
```

3. **Manually add dependencies (in requirements.txt) to pyproject.toml:**
```bash
   uv sync
```

4. **Run the API:**
```bash
   uv run fastapi dev main.py
```

The API will be available locally at `http://localhost:8000` and the OpenAPI docs will be available at `http://localhost:8000/docs`

## References
As stated, the ML model used was trained by Tunstall, Leandro Von Werra and Wolf (2022) in their book Natural Language Processing with Transformers and is publically accessible through the Hugging Face platform.
- Huggingface.co. (2024). transformersbook/distilbert-base-uncased-finetuned-emotion · Hugging Face. [online] Available at: https://huggingface.co/transformersbook/distilbert-base-uncased-finetuned-emotion [Accessed 9 Apr. 2026].
- Tiangolo.com. (2024). FastAPI. [online] Available at: https://fastapi.tiangolo.com/#license.
- Tunstall, L., Leandro von Werra and Wolf, T. (2022). Natural Language Processing with Transformers. ‘O’Reilly Media, Inc.’
