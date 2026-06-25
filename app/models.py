from app.extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    estimated_score = db.Column(db.Float, default=0.0)
    streak = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    submissions = db.relationship('WritingSubmission', backref='author', lazy=True)

    # Password management methods
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class WritingSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task_type = db.Column(db.String(50)) # 'Email' or 'Survey'
    prompt_used = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)
    word_count = db.Column(db.Integer)
    time_spent_seconds = db.Column(db.Integer)
    estimated_score = db.Column(db.Float)
    feedback_json = db.Column(db.Text) # Store AI feedback as JSON string
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

# --- EXCEL IMPORTED MODELS (Read-Only Runtime Data) ---

class VocabularyWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(50))
    difficulty = db.Column(db.Integer)
    definition = db.Column(db.Text)
    synonyms = db.Column(db.String(200)) # Comma separated
    example_sentence = db.Column(db.Text)
    celpip_usefulness_score = db.Column(db.Integer)

class Connector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    connector = db.Column(db.String(100), unique=True)
    category = db.Column(db.String(50)) # Addition, Contrast, etc.
    meaning = db.Column(db.String(200))
    example = db.Column(db.Text)
    difficulty = db.Column(db.Integer)

class Band12Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_type = db.Column(db.String(50))
    topic = db.Column(db.String(100))
    prompt = db.Column(db.Text)
    response = db.Column(db.Text)
    highlighted_connectors = db.Column(db.Text) # JSON list
    highlighted_vocabulary = db.Column(db.Text) # JSON list

class Phrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50)) # e.g., 'Email Intro', 'Survey Conclusion'
    difficulty = db.Column(db.Integer)

class PracticeTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_type = db.Column(db.String(50)) # 'Email' or 'Survey'
    context = db.Column(db.Text, nullable=False)
    data = db.Column(db.Text) # JSON string containing bullets or options

class GameScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    game_mode = db.Column(db.String(50), default="VocabDrop")
    score = db.Column(db.Integer, nullable=False)
    accuracy = db.Column(db.Float)
    highest_combo = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    user = db.relationship('User', backref=db.backref('game_scores', lazy=True))