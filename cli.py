import argparse
import json
from sentiment_analyzer import SentimentAnalyzer

def main():
    parser = argparse.ArgumentParser(description='Analyze sentiment of a review using Groq LLM with Llama3 70B model')
    parser.add_argument('review', nargs='?', help='The review text to analyze')
    parser.add_argument('--file', '-f', help='Path to a file containing the review text')
    parser.add_argument('--output', '-o', choices=['text', 'json'], default='text', help='Output format (text or json)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show detailed analysis')
    
    args = parser.parse_args()
    
    # Get review text
    review_text = ""
    if args.review:
        review_text = args.review
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                review_text = f.read()
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return
    else:
        print("Please provide a review text or a file containing the review.")
        return
    
    # Analyze sentiment
    analyzer = SentimentAnalyzer()
    result = analyzer.analyze_sentiment_structured(review_text)
    
    # Output results
    if args.output == 'json':
        if not args.verbose:
            # Remove raw result for non-verbose output
            if 'raw_result' in result:
                del result['raw_result']
        print(json.dumps(result, indent=2))
    else:
        if result["success"]:
            print(f"Sentiment: {result['sentiment']}")
            print(f"Score: {result['score']}")
            print(f"Reasoning: {result['reasoning']}")
            
            if args.verbose:
                print("\nRubric Analysis:")
                print(result['rubric_analysis'])
                print("\nRaw Result:")
                print(result['raw_result'])
        else:
            print(f"Error: {result['error']}")

if __name__ == "__main__":
    main() 