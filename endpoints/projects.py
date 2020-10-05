from flask import jsonify, make_response, request, Blueprint
import json
from repository.project import select_projects, insert_project, insert_task, select_tasks

projects_endpoints = Blueprint('projects_endpoints', __name__)


def obj_to_dict(obj):
    print(obj.__dict__)
    return obj.__dict__


@projects_endpoints.route('/api/v1/projects', methods=['GET'])
def get_projects():
    return make_response(json.dumps(select_projects(), default=obj_to_dict), 200)


@projects_endpoints.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
    return make_response(json.dumps(select_tasks(), default=obj_to_dict), 200)


@projects_endpoints.route('/api/v1/projects', methods=['POST'])
def create_project():
    json_data = request.get_json()
    project_id = json_data['project_id']
    project_name = json_data['project_name']
    project_type = json_data['project_type']
    insert_project(project_id, project_name, project_type)
    return make_response(jsonify({'message': 'project created'}), 201)


@projects_endpoints.route('/api/v1/projects_detailed', methods=['POST'])
def create_project_detailed():
    json_data = request.get_json()
    project_id = json_data['project_id']
    project_name = json_data['project_name']
    project_type = json_data['project_type']
    tasks = json_data['tasks']
    insert_project(project_id, project_name, project_type)
    for task in tasks:
        task_id = task['task_id']
        task_type = task['task_type']
        labels = task['labels']
        project_id = task['project_id']
        insert_task(task_id=task_id,
                    task_type=task_type,
                    labels=labels,
                    project_id=project_id)
    return make_response(jsonify({'message': 'project created'}), 201)


@projects_endpoints.route('/api/v1/tasks', methods=['POST'])
def create_task():
    json_data = request.get_json()
    task_id = json_data['task_id']
    task_type = json_data['task_type']
    labels = json_data['labels']
    project_id = json_data['project_id']
    insert_task(task_id=task_id,
                task_type=task_type,
                labels=labels,
                project_id=project_id)
    return make_response({'message': 'task created'}, 201)