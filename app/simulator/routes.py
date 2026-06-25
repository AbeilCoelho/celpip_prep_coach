import json
import os
import random

from flask import Blueprint, abort, jsonify, render_template, request, url_for
from flask_login import current_user, login_required
from groq import Groq

from app.extensions import db
from app.models import WritingSubmission, PracticeTask
from app.services.scoring_engine import evaluate_submission

simulator = Blueprint('simulator', __name__)

# Global prompts for the session (In a real app, pick randomly from DB)
EMAIL_PROMPT = {
    "context": "You recently bought a laptop from an online store, but it arrived damaged.",
    "bullets": [
        "Explain what you bought and when.",
        "Describe the damage to the laptop.",
        "State what action you expect the store to take."
    ]
}

SURVEY_PROMPT = {
    "context": "Your city is considering changing the speed limit on residential streets from 50 km/h to 30 km/h to improve safety.",
    "option_a": "Leave the speed limit at 50 km/h.",
    "option_b": "Reduce the speed limit to 30 km/h."
}

@simulator.route('/email')
@login_required
def task1_email():
    # Fetch all Email tasks from the DB
    tasks = PracticeTask.query.filter_by(task_type='Email').all()
    
    if tasks:
        # Pick a random task
        task = random.choice(tasks)
        # Parse the JSON string from the Excel file back into a dictionary
        prompt_data = json.loads(task.data)
        
        prompt = {
            "context": task.context,
            "bullets": prompt_data.get("bullets", [])
        }
    else:
        # Fallback just in case DB is empty
        prompt = {"context": "Database empty. Run seed_data.py", "bullets": ["No bullets loaded."]}
        
    return render_template('simulator/task1.html', prompt=prompt)

@simulator.route('/survey')
@login_required
def task2_survey():
    # Fetch all Survey tasks from the DB
    tasks = PracticeTask.query.filter_by(task_type='Survey').all()
    
    if tasks:
        # Pick a random task
        task = random.choice(tasks)
        # Parse the JSON string from the Excel file back into a dictionary
        prompt_data = json.loads(task.data)
        
        prompt = {
            "context": task.context,
            "option_a": prompt_data.get("option_a", ""),
            "option_b": prompt_data.get("option_b", "")
        }
    else:
         # Fallback
        prompt = {"context": "Database empty. Run seed_data.py", "option_a": "Error", "option_b": "Error"}
        
    return render_template('simulator/task2.html', prompt=prompt)

@simulator.route('/submit/<task_type>', methods=['POST'])
@login_required
def submit_task(task_type):
    data = request.json
    content = data.get('content')
    time_spent = data.get('time_spent')
    
    # NEW: The frontend should send the prompt context so the AI knows what to grade against
    prompt_context = data.get('prompt_context', 'No context provided.')
    
    db_task_type = 'Email' if task_type.lower() == 'email' else 'Survey'
    
    # Call Groq AI using llama-3.3-70b-versatile
    evaluation = evaluate_submission(content, task_type=db_task_type, prompt_context=prompt_context)
    
    submission = WritingSubmission(
        user_id=current_user.id,
        task_type=db_task_type,
        content=content,
        word_count=len(content.split()),
        time_spent_seconds=time_spent,
        estimated_score=evaluation['estimated_score'],
        feedback_json=json.dumps(evaluation) 
    )
    db.session.add(submission)
    
    # Update Stats
    current_user.estimated_score = evaluation['estimated_score']
    current_user.streak += 1 
    db.session.commit()
    
    return jsonify({
        "status": "success",
        "redirect_url": url_for('simulator.results', submission_id=submission.id)
    })

@simulator.route('/results/<int:submission_id>')
@login_required
def results(submission_id):
    submission = WritingSubmission.query.get_or_404(submission_id)
    if submission.user_id != current_user.id:
        abort(403)
        
    feedback = json.loads(submission.feedback_json)
    return render_template('simulator/results.html', submission=submission, feedback=feedback)

@simulator.route('/api/assistant', methods=['POST'])
@login_required
def writing_assistant():
    """Takes text and returns AI-suggested improvements."""
    data = request.json
    text = data.get('text', '')
    
    if not text or len(text.split()) < 5:
        return jsonify({"suggestion": "Keep typing! I need a bit more text to help."})

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return jsonify({"suggestion": "Groq API key missing. Cannot provide suggestions."})

    client = Groq(api_key=api_key)
    prompt = f"Rewrite the following sentence/paragraph to sound like a Band 12 CELPIP response. Use advanced vocabulary and strong connectors. Keep it concise. ONLY output the improved text, nothing else.\n\nOriginal: {text}"

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile", # Using 8b for ultra-fast, real-time responses
            temperature=0.3
        )
        return jsonify({"suggestion": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"suggestion": "AI Assistant is currently resting."})