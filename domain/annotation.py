class Asset:
    def __init__(self, file_name, path):
        self.file_name = file_name
        self.path = path

    def __eq__(self, other):
        return self.file_name == other.file_name \
                and self.path == other.path

    def __repr__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

class Annotation:
    def __init__(self, task_id, file_name, email, label):
        self.task_id = task_id
        self.file_name = file_name
        self.email = email
        self.label = label

    def __eq__(self, other):
        return self.task_id == other.task_id \
               and self.file_name == other.file_name \
               and self.email == other.email \
               and self.label == other.labe

    def __repr__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])