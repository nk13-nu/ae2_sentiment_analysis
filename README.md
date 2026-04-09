# Transformer-based Sentiment Analysis API
This project is a REST API for sentiment analysis which uses a transformer-based machine learning model to classify the emotional tone of input text. It is intended to be used by organisations to understand user feedback left by users.


## Design



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
