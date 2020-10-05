from flask import Flask, jsonify, make_response, request, Blueprint
from flask_cors import CORS
from endpoints import projects_endpoints, users_endpoints

app = Flask(__name__)
CORS(app)
app.register_blueprint(projects_endpoints)
app.register_blueprint(users_endpoints)

if __name__ == '__main__':
    app.run(debug=True)