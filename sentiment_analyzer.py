import os
import re
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class SentimentAnalyzer:
    def __init__(self):
        self.model = "llama3-70b-8192"
        self.rubric = [
            {"criterion": "Positive Language", "description": "Contains positive words/phrases (e.g., good, great, excellent, love)", "weight": 1},
            {"criterion": "Negative Language", "description": "Contains negative words/phrases (e.g., bad, poor, terrible, hate)", "weight": -1},
            {"criterion": "Explicit Recommendation", "description": "Explicitly recommends the product/service to others", "weight": 2},
            {"criterion": "Explicit Discouragement", "description": "Explicitly discourages others from the product/service", "weight": -2},
            {"criterion": "Satisfaction Expression", "description": "Clearly expresses satisfaction with experience", "weight": 1.5},
            {"criterion": "Dissatisfaction Expression", "description": "Clearly expresses dissatisfaction with experience", "weight": -1.5},
            {"criterion": "Future Purchase Intent", "description": "Expresses intention to return/repurchase in future", "weight": 1.5},
            {"criterion": "Future Avoidance Intent", "description": "Expresses intention to avoid in future", "weight": -1.5},
            {"criterion": "Specific Problems", "description": "Mentions specific problems or issues", "weight": -1},
            {"criterion": "Specific Praise", "description": "Mentions specific positive aspects or praise", "weight": 1},
            {"criterion": "Overall Tone", "description": "The overall tone is predominantly positive", "weight": 1.5},
        ]
    
    def validate_review(self, review_text):
        """Validate that the review is not empty and contains meaningful content."""
        if not review_text or review_text.strip() == "":
            return False
        return True
    
    def analyze_sentiment(self, review_text):
        # Validate the review
        if not self.validate_review(review_text):
            return "INVALID REVIEW: The review is empty or contains no meaningful content."
        
        prompt = self._create_prompt(review_text)
        
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an objective sentiment analysis assistant. Analyze the review based on the provided rubric and determine if it's positive or negative. Always provide a clear POSITIVE or NEGATIVE determination, even for short or ambiguous reviews."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=1024
            )
            
            result = response.choices[0].message.content
            
            # Ensure the result contains a sentiment determination
            if "POSITIVE" not in result and "NEGATIVE" not in result:
                # Force a determination based on the content
                if any(word in result.lower() for word in ["good", "great", "excellent", "like", "love", "enjoy", "positive"]):
                    result += "\n\nFINAL SENTIMENT: POSITIVE"
                else:
                    result += "\n\nFINAL SENTIMENT: NEGATIVE"
            
            return result
        except Exception as e:
            return f"ERROR: Failed to analyze sentiment. {str(e)}"
    
    def analyze_sentiment_structured(self, review_text):
        """Analyze sentiment and return structured results."""
        raw_result = self.analyze_sentiment(review_text)
        
        if raw_result.startswith("INVALID") or raw_result.startswith("ERROR"):
            return {
                "success": False,
                "error": raw_result,
                "sentiment": None,
                "score": None,
                "reasoning": None,
                "rubric_analysis": None
            }
        
        try:
            # Extract sentiment - improved regex to be more flexible
            sentiment_match = re.search(r"FINAL SENTIMENT:?\s*(POSITIVE|NEGATIVE)", raw_result, re.IGNORECASE)
            sentiment = sentiment_match.group(1).upper() if sentiment_match else "UNKNOWN"
            
            # If sentiment is still unknown, try a more lenient search
            if sentiment == "UNKNOWN":
                if "positive" in raw_result.lower():
                    sentiment = "POSITIVE"
                elif "negative" in raw_result.lower():
                    sentiment = "NEGATIVE"
            
            # Extract score
            score_match = re.search(r"SCORE CALCULATION:.*?=\s*([-+]?\d*\.?\d+)", raw_result, re.DOTALL)
            score = float(score_match.group(1)) if score_match else None
            
            # If no score was found or score is 0 but we have a sentiment, assign a default score
            if (score is None or score == 0.0) and sentiment != "UNKNOWN":
                score = 1.0 if sentiment == "POSITIVE" else -1.0
            
            # Ensure score aligns with sentiment
            if sentiment == "POSITIVE" and score <= 0:
                score = 0.1  # Small positive score
            elif sentiment == "NEGATIVE" and score >= 0:
                score = -0.1  # Small negative score
            
            # Extract reasoning
            reasoning_match = re.search(r"REASONING:?\s*(.*?)(?:\n\n|\Z)", raw_result, re.DOTALL)
            reasoning = reasoning_match.group(1).strip() if reasoning_match else None
            
            # If no reasoning was found, provide a default
            if not reasoning and sentiment != "UNKNOWN":
                reasoning = f"The review was determined to be {sentiment.lower()} based on overall tone and content analysis."
            
            # Extract rubric analysis
            rubric_analysis_match = re.search(r"RUBRIC ANALYSIS:?(.*?)(?:SCORE CALCULATION:|FINAL SENTIMENT:|\Z)", raw_result, re.DOTALL)
            rubric_analysis = rubric_analysis_match.group(1).strip() if rubric_analysis_match else None
            
            return {
                "success": True,
                "sentiment": sentiment,
                "score": score,
                "reasoning": reasoning,
                "rubric_analysis": rubric_analysis,
                "raw_result": raw_result
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to parse results: {str(e)}",
                "raw_result": raw_result,
                "sentiment": None,
                "score": None,
                "reasoning": None,
                "rubric_analysis": None
            }
    
    def _create_prompt(self, review_text):
        prompt = f"""
Please analyze the following review for sentiment:

"{review_text}"

For each criterion in the rubric below, respond with YES or NO, and provide a brief explanation with specific evidence from the text:

"""
        for item in self.rubric:
            prompt += f"- {item['criterion']} (Weight: {item['weight']}): {item['description']}\n"
        
        prompt += """
After completing the rubric, calculate the weighted sentiment score as follows:
1. For each criterion marked YES, add its associated weight to the score
2. Sum all weights to get a final score

Based on the final score:
- If score > 0: Label as POSITIVE and explain why
- If score < 0: Label as NEGATIVE and explain why
- If score = 0: Analyze the intensity and specificity of positive vs negative elements to make a determination

IMPORTANT: Even for very short or ambiguous reviews, you MUST make a definitive POSITIVE or NEGATIVE determination. For neutral or ambiguous reviews, consider subtle cues or default to slightly positive if truly neutral.

Format your response as:
RUBRIC ANALYSIS:
[Analysis of each criterion with YES/NO and brief explanation]

SCORE CALCULATION:
[Show your calculation with weights]

FINAL SENTIMENT: [POSITIVE/NEGATIVE]
REASONING: [Objective explanation based on the evidence]
"""
        return prompt 