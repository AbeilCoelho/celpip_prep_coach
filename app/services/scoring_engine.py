import os
import json
from groq import Groq

def evaluate_submission(content, task_type, prompt_context=""):
    """
    Evaluates CELPIP writing using GROQ (Llama 3 70B).
    Returns a dictionary containing the estimated score, metrics, and feedback.
    """
    api_key = os.environ.get("GROQ_API_KEY")
    
    if api_key:
        return _call_groq_api(content, task_type, prompt_context, api_key)
    else:
        print("WARNING: No GROQ_API_KEY found. Falling back to mock scoring.")
        return _mock_evaluation(content, task_type)

def _call_groq_api(content, task_type, prompt_context, api_key):
    client = Groq(api_key=api_key)
    
    system_prompt = f"""You are a strict, expert CELPIP Writing Examiner. 
Your job is to evaluate a {task_type} submission.

Context/Prompt the user was responding to:
{prompt_context}

Evaluate the user's submission strictly on the standard CELPIP scale (4.0 to 12.0).
Focus on:
1. Task Fulfillment: Did they answer all parts of the prompt? Is the tone appropriate? Is the word count roughly 150-200 words?
2. Vocabulary: Did they use advanced, precise vocabulary or basic words?
3. Grammar: Are there grammatical errors? Is there a variety of complex sentence structures?
4. Organization: Did they use paragraphs properly? Did they use advanced connectors (e.g., furthermore, consequently)?

You MUST output ONLY a JSON object. Do not include markdown formatting (like ```json). Just output the raw JSON object.

Structure MUST be exactly:
{{
  "estimated_score": 9.5,
  "metrics": {{
    "task_fulfillment": 9.0,
    "vocabulary": 10.0,
    "grammar": 9.5,
    "organization": 9.5
  }},
  "feedback": [
    "Specific feedback about their task fulfillment.",
    "Specific feedback about their vocabulary/grammar.",
    "A suggestion for better connectors or organization."
  ],
  "improved_version": "Provide a complete Band 12 rewrite of their text."
}}"""

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": content}
            ],
            model="llama-3.3-70b-versatile", # Llama 3 70B is excellent for grading and instruction following
            temperature=0.2, # Low temperature for consistent grading
            response_format={"type": "json_object"} # Forces JSON output
        )
        
        # Parse the JSON response
        result_json = response.choices[0].message.content
        return json.loads(result_json)

    except Exception as e:
        print(f"Groq API Error: {e}")
        # Fallback if API fails
        return _mock_evaluation(content, task_type)

def _mock_evaluation(content, task_type):
    # (Keep your existing mock evaluation code here as a fallback)
    base_score = 7.0
    if len(content.split()) > 150: base_score += 1.0
    
    return {
        "estimated_score": round(base_score),
        "metrics": {"task_fulfillment": base_score, "vocabulary": base_score, "grammar": base_score, "organization": base_score},
        "feedback": ["This is mock feedback.", "Set your GROQ_API_KEY to see real AI feedback."],
        "improved_version": "Mock improved version."
    }