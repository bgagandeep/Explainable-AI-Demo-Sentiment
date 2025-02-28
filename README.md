# Sentiment Analysis with Groq LLM and Llama3 70B

This project implements a robust sentiment analysis system using Groq's API with the Llama3 70B model. The system analyzes user reviews, determines if they're positive or negative, and provides objective reasoning based on a detailed weighted rubric.

## Features

- **Objective Analysis**: Uses a weighted rubric with 11 criteria to mathematically determine sentiment
- **Detailed Reasoning**: Provides clear explanations for sentiment determinations
- **Multiple Interfaces**: Includes both interactive CLI and command-line tools
- **Structured Output**: Returns sentiment analysis in structured format with scores
- **Robust Handling**: Manages edge cases like empty reviews, very short reviews, and non-English content
- **Comprehensive Testing**: Includes basic and comprehensive test suites

## Setup

1. Clone this repository
2. Install the required packages:
   ```
   pip install groq python-dotenv
   ```
3. Create a `.env` file in the project root with your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

### Interactive Testing Mode

Run the interactive test mode to analyze reviews:
```bash
python app.py
```
When prompted, enter a review to analyze. The system will show:
1. Sentiment determination (Positive/Negative/Neutral)
2. Total weighted score (0-100)
3. Analysis reasoning based on the rubric
4. Confidence level in the assessment
5. Flagged special cases (if any)

### Command-line Tool

The command-line tool allows you to analyze multiple reviews at once: 

## Interpreting Results

Sample output:

## About Explainable AI

This project aims to make LLMs explainable by providing clear and detailed reasoning for sentiment determinations. The weighted rubric used in the analysis contributes to transparency by breaking down the components of sentiment determination and providing a clear understanding of the reasoning process.

This approach helps users understand how the system's structure contributes to transparency and makes the LLM's decision-making process more understandable. 