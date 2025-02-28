import unittest
from sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SentimentAnalyzer()
        self.test_cases = [
            {
                "review": "I absolutely loved this product! It works perfectly and exceeded my expectations. I'll definitely buy it again and recommend it to all my friends.",
                "expected_sentiment": "POSITIVE"
            },
            {
                "review": "This was a terrible experience. The product broke after two days and customer service was unhelpful. I regret this purchase and won't be buying from them again.",
                "expected_sentiment": "NEGATIVE"
            },
            {
                "review": "The product has some good features, but it's overpriced and the battery life is disappointing. Not sure if I would recommend it.",
                "expected_sentiment": None  # Could be either positive or negative
            },
            {
                "review": "The product arrived on time. It has a blue color and metal finish. It comes with a user manual.",
                "expected_sentiment": None  # Neutral, but should still make a determination
            },
            {
                "review": "It's okay.",
                "expected_sentiment": None  # Very short, but should still make a determination
            },
            {
                "review": "",
                "expected_sentiment": "INVALID"  # Empty review
            },
            {
                "review": "Me encantó este producto. Es fantástico.",  # Spanish: "I loved this product. It's fantastic."
                "expected_sentiment": "POSITIVE"
            },
            {
                "review": "This product is amazing! However, it has some serious flaws that make it unusable. The design is beautiful though.",
                "expected_sentiment": None  # Mixed review with strong positives and negatives
            }
        ]
    
    def test_all_cases(self):
        for i, case in enumerate(self.test_cases):
            print(f"Testing case {i+1}: {case['review'][:30]}...")
            
            result = self.analyzer.analyze_sentiment_structured(case['review'])
            
            # Check if the analysis was successful (unless it's an empty review)
            if case['expected_sentiment'] != "INVALID":
                self.assertTrue(result['success'], f"Case {i+1} failed: Analysis was not successful")
            
            # If we have an expected sentiment, check it
            if case['expected_sentiment'] is not None:
                if case['expected_sentiment'] == "INVALID":
                    self.assertFalse(result['success'], f"Case {i+1} failed: Empty review should be invalid")
                else:
                    self.assertEqual(result['sentiment'], case['expected_sentiment'], 
                                    f"Case {i+1} failed: Expected {case['expected_sentiment']}, got {result['sentiment']}")
            
            # For cases where we don't specify the expected sentiment, just check that it made a determination
            else:
                self.assertIn(result['sentiment'], ["POSITIVE", "NEGATIVE"], 
                             f"Case {i+1} failed: No sentiment determination made")
            
            # Check that we have a score for valid reviews
            if case['expected_sentiment'] != "INVALID" and result['success']:
                self.assertIsNotNone(result['score'], f"Case {i+1} failed: No score provided")
                
                # Check that the score matches the sentiment
                if result['sentiment'] == "POSITIVE":
                    self.assertGreater(result['score'], 0, f"Case {i+1} failed: Positive sentiment with non-positive score")
                elif result['sentiment'] == "NEGATIVE":
                    self.assertLess(result['score'], 0, f"Case {i+1} failed: Negative sentiment with non-negative score")
            
            print(f"Case {i+1} passed!")

if __name__ == "__main__":
    unittest.main() 