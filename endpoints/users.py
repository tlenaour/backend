from flask import jsonify, make_response, request, Blueprint
import json
from repository.users import select_projects_roles_by_user
users_endpoints = Blueprint('users_endpoints', __name__)


def obj_to_dict(obj):
    print(obj.__dict__)
    return obj.__dict__


@users_endpoints.route('/api/v1/user_roles/<string:email>', methods=['GET'])
def get_projects(email):
    return make_response(json.dumps(select_projects_roles_by_user(email), default=obj_to_dict), 200)
