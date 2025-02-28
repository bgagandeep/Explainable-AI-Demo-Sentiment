import unittest
from sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SentimentAnalyzer()
    
    def test_positive_review(self):
        review = "I absolutely loved this product! It works perfectly and exceeded my expectations. I'll definitely buy it again and recommend it to all my friends."
        result = self.analyzer.analyze_sentiment(review)
        self.assertIn("POSITIVE", result)
    
    def test_negative_review(self):
        review = "This was a terrible experience. The product broke after two days and customer service was unhelpful. I regret this purchase and won't be buying from them again."
        result = self.analyzer.analyze_sentiment(review)
        self.assertIn("NEGATIVE", result)
    
    def test_mixed_review(self):
        review = "The product has some good features, but it's overpriced and the battery life is disappointing. Not sure if I would recommend it."
        result = self.analyzer.analyze_sentiment(review)
        # We'll check that it contains a final sentiment judgment
        self.assertTrue("POSITIVE" in result or "NEGATIVE" in result)
    
    def test_neutral_review(self):
        review = "The product arrived on time. It has a blue color and metal finish. It comes with a user manual."
        result = self.analyzer.analyze_sentiment(review)
        # Should still make a determination
        self.assertTrue("POSITIVE" in result or "NEGATIVE" in result)
    
    def test_very_short_review(self):
        review = "It's okay."
        result = self.analyzer.analyze_sentiment(review)
        self.assertTrue("POSITIVE" in result or "NEGATIVE" in result)
    
    def test_empty_review(self):
        review = ""
        result = self.analyzer.analyze_sentiment(review)
        self.assertIn("INVALID", result)
    
    def test_non_english_review(self):
        review = "Me encantó este producto. Es fantástico."  # Spanish
        result = self.analyzer.analyze_sentiment(review)
        self.assertTrue("POSITIVE" in result or "NEGATIVE" in result)

if __name__ == "__main__":
    unittest.main() 