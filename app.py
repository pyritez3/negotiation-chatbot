from flask import Flask, request, jsonify
from transformers import pipeline
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

sid = SentimentIntensityAnalyzer()  # sentiment analyzer
model = pipeline("text-generation", model="distilgpt2")  # language model

BASE_PRICE = 100  # Pre-defined pricing
DISCOUNT_THRESHOLD = 20  # Minimum discount

def analyze_sentiment(user_input):
    scores = sid.polarity_scores(user_input)  # Analyze sentiment scores
    return scores['compound']

def negotiate_price(user_price):
    if user_price < BASE_PRICE - DISCOUNT_THRESHOLD:
        return f"Your offer of {user_price} is too low. Can you do better?"
    elif user_price > BASE_PRICE + DISCOUNT_THRESHOLD:
        return f"Your offer of {user_price} is too high. How about we settle at {BASE_PRICE}?"
    else:
        discount = BASE_PRICE - user_price
        return f"Great! I can accept your offer of {user_price} with a discount of {discount}."

@app.route('/negotiate', methods=['POST'])
def negotiate():
    data = request.json
    user_price = data.get('price', BASE_PRICE)  # user price
    user_message = data.get('message', '')  # user message

    sentiment_score = analyze_sentiment(user_message)  #  sentiment ana;ysis
    if sentiment_score > 0.5:
        response = negotiate_price(user_price - 5)  # Better deals for positive sentiment
    elif sentiment_score < -0.5:
        response = negotiate_price(user_price + 5)  # Worse deals for negative sentiment
    else:
        response = negotiate_price(user_price)  # Neutral sentiment response

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
