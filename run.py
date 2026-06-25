from app import create_app
from app.extensions import db

app = create_app()

if __name__ == '__main__':
    # Run in debug mode for local development
    app.run(debug=False, host='192.168.4.106', port=5000)