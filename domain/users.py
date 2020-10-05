from enum import Enum


class ProjectRole(Enum):
    SUPERUSER = 'superuser'
    ADMIN_PLATFORM = 'admin_platform'
    ADMIN_PROJECT = 'admin_project'
    ANNOTATOR = 'annotator'


class User:
    def __init__(self, email, last_name, first_name, roles_per_projects=None):
        self.email = email
        self.last_name = last_name
        self.first_name = first_name
        self.rolers_per_projects = roles_per_projects

    def __eq__(self, other):
        return self.email == other.email \
                and self.last_name == other.last_name \
                and self.first_name == other.first_name \
                and self.rolers_per_projects == other.roles_per_projects

    def __repr__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])


class UserProjectRole:
    def __init__(self, email, project_id, role):
        self.email = email
        self.project_id = project_id
        self.role = role

    def __eq__(self, other):
        return self.email == other.email \
                and self.project_id == other.project_id \
                and self.role == other.role

    def __repr__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])