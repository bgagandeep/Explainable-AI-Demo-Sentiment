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

### Interactive Mode

The interactive mode allows you to analyze reviews one at a time: 