"""
Projects management
"""

from yoyo import step

__depends__ = {}

steps = [
    step("CREATE TABLE project(\
         project_id varchar(25) PRIMARY KEY,\
         project_name varchar(40) ,\
         creation_date date,\
         project_type varchar(25));", "DROP  TABLE project;"),
    step("CREATE TABLE task(\
         task_id varchar(25) PRIMARY KEY,\
         task_type varchar(25),\
         labels text[],\
         project_id varchar(25),\
        CONSTRAINT fk_project FOREIGN KEY(project_id) REFERENCES project(project_id));", "DROP  TABLE task;")
]
