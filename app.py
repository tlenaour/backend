from flask import Flask, jsonify, make_response, request, Blueprint
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def load_data(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data



projects_data = load_data('projects.json')
annotatios_data = load_data('annotations.json')
image_to_annotate_data = load_data('images_to_annotate.json')
@app.route('/api/v1/projects',methods=['GET'])
def get_projects():
    return make_response(jsonify(projects_data), 200)

@app.route('/api/v1/projects',methods=['POST'])
def create_project():
    json_data = request.get_json()
    projects_data.append(json_data)
    return make_response(jsonify(projects_data), 200)

@app.route('/api/v1/annotations',methods=['GET'])
def get_annotations():
    return make_response(jsonify(annotatios_data), 200)

@app.route('/api/v1/images_to_annotate',methods=['GET'])
def get_image_to_annotate():
    return make_response(jsonify(image_to_annotate_data), 200)



if __name__ == '__main__':
    app.run(debug=True)