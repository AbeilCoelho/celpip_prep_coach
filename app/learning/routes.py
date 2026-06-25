import json
import random
import re

from flask import jsonify, render_template, request
from flask_login import current_user, login_required
from sqlalchemy import desc

from app.extensions import db
from app.learning import learning
from app.models import Band12Example, GameScore, Phrase, VocabularyWord

@learning.route('/vocab-drop')
@login_required
def vocab_drop():
    return render_template('learning/vocab_drop.html')

@learning.route('/api/vocab-drop/data')
@login_required
def vocab_drop_data():
    """Fetches words and creates blanked-out sentences for the game."""
    words = VocabularyWord.query.all()
    game_data = []
    
    for w in words:
        if not w.example_sentence: continue
        
        # Replace the word in the sentence with blanks (case insensitive)
        pattern = re.compile(re.escape(w.word), re.IGNORECASE)
        blanked_sentence = pattern.sub("________", w.example_sentence)
        
        # Only add if the word was actually found and replaced in the example
        if "________" in blanked_sentence:
            game_data.append({
                "word": w.word.lower(),
                "sentence": blanked_sentence,
                "definition": w.definition,
                "category": w.category
            })
            
    # Shuffle and return
    random.shuffle(game_data)
    return jsonify(game_data)

@learning.route('/api/vocab-drop/save', methods=['POST'])
@login_required
def vocab_drop_save():
    """Saves the game score."""
    data = request.json
    
    score = GameScore(
        user_id=current_user.id,
        score=data.get('score', 0),
        accuracy=data.get('accuracy', 0),
        highest_combo=data.get('highest_combo', 0)
    )
    db.session.add(score)
    db.session.commit()
    
    return jsonify({"status": "success"})

@learning.route('/leaderboard')
@login_required
def leaderboard():
    """Global Leaderboard."""
    top_scores = GameScore.query.filter_by(game_mode="VocabDrop").order_by(desc(GameScore.score)).limit(10).all()
    return render_template('learning/leaderboard.html', scores=top_scores)

@learning.route('/vocabulary')
def vocabulary_trainer():
    words = VocabularyWord.query.all()
    
    if not words:
        fallback_data = [
            {"word": "Advantageous", "category": "General", "definition": "Providing an advantage; favorable.", "example_sentence": "Working from home is highly advantageous.", "difficulty": 8},
            {"word": "Consequently", "category": "Connector", "definition": "As a result.", "example_sentence": "He was late; consequently, he missed the meeting.", "difficulty": 7},
            {"word": "Substantial", "category": "General", "definition": "Of considerable importance, size, or worth.", "example_sentence": "There was a substantial increase in profits.", "difficulty": 9}
        ]
        return render_template('learning/vocab_trainer.html', words=fallback_data)

    # Shuffle the words so the user gets a different order every time
    random.shuffle(words)
    
    # Format the data for the frontend
    vocab_list = [
        {
            "word": w.word, 
            "category": w.category,
            "definition": w.definition, 
            "example_sentence": w.example_sentence, 
            "difficulty": w.difficulty
        } for w in words
    ]
    
    return render_template('learning/vocab_trainer.html', words=vocab_list)

@learning.route('/phrases')
def phrase_bank():
    phrases = Phrase.query.all()
    # Fallback if Excel isn't loaded
    if not phrases:
        phrases = [
            Phrase(phrase="I am writing to express my dissatisfaction regarding...", category="Complaint Email", difficulty=7),
            Phrase(phrase="The primary reason for my preference is that...", category="Survey Argument", difficulty=6),
            Phrase(phrase="Furthermore, it is crucial to consider the long-term impact.", category="Survey Body", difficulty=9)
        ]
    return render_template('learning/phrase_bank.html', phrases=phrases)

@learning.route('/band12')
def band12_library():
    examples = Band12Example.query.all()
    if not examples:
        examples = [
            Band12Example(task_type="Email", topic="Noise Complaint", prompt="Complain about a neighbor.", response="Dear Building Manager,\n\nI am writing to formally express my concern regarding the excessive noise originating from unit 4B. Furthermore, this disruption has significantly impacted my ability to work from home. Consequently, I kindly request that you address this matter immediately.\n\nThank you for your prompt attention to this issue.\n\nSincerely,\nJohn Doe")
        ]
    return render_template('learning/band12.html', examples=examples)