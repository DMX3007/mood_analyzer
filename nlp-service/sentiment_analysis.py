from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
# sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
# sentiment_analyzer = pipeline("sentiment-analysis", model="DeepPavlov/rubert-base-cased-sentiment")
# Use an open-access model for Russian sentiment analysis
# sentiment_analyzer = pipeline("sentiment-analysis", model="cointegrated/rubert-tiny2")
sentiment_analyzer = pipeline("sentiment-analysis", model="sismetanin/sbert-ru-sentiment-rureviews")


@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text')
    sentiment_result = sentiment_analyzer(text)
    return jsonify(sentiment_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
