from flask import Flask
from flask_cors import CORS
from trends_api import trends_blueprint

app = Flask(__name__)
CORS(app)  # Allow frontend (Vue) to access this API

# Register blueprint
app.register_blueprint(trends_blueprint)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
