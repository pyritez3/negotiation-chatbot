# Negotiation Chatbot

## Overview
This project implements a negotiation chatbot that simulates a negotiation process between a customer and a supplier. It uses a combination of the Hugging Face Transformers library for text generation and VADER for sentiment analysis.

## Technologies Used
- Python
- Flask
- Hugging Face Transformers
- NLTK (VADER for sentiment analysis)

## Installation

1. Clone the repository:
   
```bash
git clone https://github.com/yourusername/negotiation-chatbot.git
 ```

2. Navigate to the project directory:

```bash
cd negotiation-chatbot
```

3. Create a virtual environment:

```bash
python -m venv negotiation-bot
negotiation-bot\Scripts\activate 
```

4. Install the required libraries:

```bash
pip install Flask torch transformers nltk
```

5. Download VADER lexicon(Python shell):

```bash
import nltk
nltk.download('vader_lexicon')
```

6. Run the Flask app:

```bash
python app.py
```

7. API Usage:

```bash
curl -X POST http://127.0.0.1:5000/negotiate -H "Content-Type: application/json" -d "{\"price\": 95, \"message\": \"I think this is a fair price.\"}"
```







