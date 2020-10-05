class Project:
    def __init__(self, project_id, project_name, project_type, tasks):
        self.project_id = project_id
        self.project_name = project_name
        self.project_type = project_type
        self.tasks = tasks

    def __eq__(self, other):
        return self.project_id == other.project_id \
                and self.project_name == other.project_name \
                and self.project_type == other.project_type \
                and self.tasks == other.tasks

    def __repr__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])


class Task:
    def __init__(self, task_id, project_id, task_type, labels):
        self.task_id = task_id
        self.project_id = project_id
        self.task_type = task_type
        self.labels = labels

    def __eq__(self, other):
        return self.task_id == other.task_id \
                and self.task_type == other.task_type \
                and self.labels == other.labels

    def __repr__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])