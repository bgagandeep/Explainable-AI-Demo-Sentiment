# Explainable AI: Sentiment Analysis with LLMs

This project demonstrates how Large Language Models can be made explainable through structured system design, using sentiment analysis as a case study. Unlike traditional machine learning systems where explainability relies on feature importance or model internals, LLM transparency requires building **auditable reasoning frameworks** around the model's capabilities.

## Why LLM Explainability is Different

Traditional approaches like SHAP values or logistic regression coefficients don't translate well to LLMs. Instead, we achieve explainability through:
1. **Structured Rubrics** - Predefined evaluation criteria that constrain and guide the model's analysis
2. **Traceable Reasoning** - Forced decomposition of decisions into measurable components
3. **Transparency Mechanisms** - Built-in confidence scoring and bias detection
4. **Contextual Grounding** - Explicit identification of cultural and linguistic context

## Key Differentiators

This implementation shows how to build explainability _around_ an LLM through:
- **Weighted Decision Framework** - Mathematical scoring system visible to end users
- **Reasoning Trace** - Clear lineage from input text to final sentiment determination  
- **Dynamic Context Handling** - Explicit identification of sarcasm, cultural references, and subjectivity
- **Confidence Calibration** - Built-in uncertainty estimation for each analysis
- **Bias Checks** - Automated detection of potential subjective language

## Features

- **Auditable Analysis**: Every sentiment determination can be traced through 11 measurable criteria
- **Structured Reasoning**: Forces the LLM to follow predefined evaluation logic
- **Transparency Layers**: Confidence scoring + bias detection + cultural context identification
- **Comparable Outputs**: Numerical scoring enables systematic quality comparisons
- **Human-AI Alignment**: Flagging system highlights where human review is recommended

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