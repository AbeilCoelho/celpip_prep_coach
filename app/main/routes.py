from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import WritingSubmission

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/dashboard')
@login_required
def dashboard():
    # Fetch all user submissions, ordered by newest first
    submissions = WritingSubmission.query.filter_by(user_id=current_user.id).order_by(WritingSubmission.created_at.desc()).all()
    
    # Get the 5 most recent for the table
    recent_subs = submissions[:5]
    
    # Prepare data for the Chart.js graph (Reverse to chronological order: Oldest to Newest)
    chart_data_points = submissions[:10][::-1]
    chart_labels = [sub.created_at.strftime('%b %d') for sub in chart_data_points]
    chart_scores = [sub.estimated_score for sub in chart_data_points]

    # Calculate overall stats
    total_sessions = len(submissions)
    avg_score = sum(sub.estimated_score for sub in submissions) / total_sessions if total_sessions > 0 else 0

    stats = {
        'streak': current_user.streak,
        'estimated_score': round(current_user.estimated_score, 1) if current_user.estimated_score else "N/A",
        'average_score': round(avg_score, 1),
        'sessions_completed': total_sessions
    }
    
    return render_template('dashboard.html', 
                           stats=stats, 
                           recent_subs=recent_subs, 
                           chart_labels=chart_labels, 
                           chart_scores=chart_scores)