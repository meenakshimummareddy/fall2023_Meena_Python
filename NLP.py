import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Subheading 1: Initialize NLTK and load data
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# Subheading 2: Define the text for sentiment analysis
text = """
Sentiment analysis, also known as opinion mining, is the process of determining the sentiment or emotional tone of text. It is widely used to analyze customer reviews, social media comments, and more.
"""

# Subheading 3: Perform sentiment analysis
sentiment_scores = sia.polarity_scores(text)

# Subheading 4: Analyze and display sentiment scores
print("Sentiment Scores:")
print(f"Positive: {sentiment_scores['pos']:.2f}")
print(f"Neutral: {sentiment_scores['neu']:.2f}")
print(f"Negative: {sentiment_scores['neg']:.2f}")
print(f"Compound: {sentiment_scores['compound']:.2f}")
