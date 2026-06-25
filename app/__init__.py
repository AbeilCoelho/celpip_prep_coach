from flask import Flask
from app.extensions import db, login_manager
from app.services.import_engine import load_excel_to_db

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    from app.main.routes import main
    from app.auth.routes import auth
    from app.simulator.routes import simulator
    from app.learning.routes import learning
    
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(simulator, url_prefix='/simulator')
    app.register_blueprint(learning, url_prefix='/learning')

    with app.app_context():
        db.create_all()
        # Trigger the Excel Import Engine
        load_excel_to_db(app)

    return app