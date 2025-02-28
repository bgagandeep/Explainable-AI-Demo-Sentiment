from sentiment_analyzer import SentimentAnalyzer
import json

def main():
    analyzer = SentimentAnalyzer()
    
    print("Welcome to the Sentiment Analyzer!")
    print("Enter a review to analyze (or 'quit' to exit):")
    
    while True:
        review = input("\nReview: ")
        if review.lower() == 'quit':
            break
        
        print("\nAnalyzing sentiment...")
        result = analyzer.analyze_sentiment_structured(review)
        
        if result["success"]:
            print("\n=== Analysis Result ===")
            print(f"Sentiment: {result['sentiment']}")
            print(f"Score: {result['score']}")
            print(f"Reasoning: {result['reasoning']}")
            
            print("\nWould you like to see the detailed rubric analysis? (y/n)")
            if input().lower() == 'y':
                print("\n=== Rubric Analysis ===")
                print(result['rubric_analysis'])
                
            print("\nWould you like to see the raw result? (y/n)")
            if input().lower() == 'y':
                print("\n=== Raw Result ===")
                print(result['raw_result'])
        else:
            print(f"\nError: {result['error']}")

if __name__ == "__main__":
    main() 