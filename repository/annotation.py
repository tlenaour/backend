from sqlalchemy import select
from config.database import metadata, connection
from domain.project import Project, Task
PROJECT_TABLE_NAME = 'project'
PROJECT_TABLE = metadata.tables[PROJECT_TABLE_NAME]

def insert_project(project_id, project_name, project_type):
    insert = PROJECT_TABLE.insert().values(project_id=project_id,
                                           project_name=project_name,
                                           project_type=project_type)
    try:
        result = connection.execute(insert)
    except Exception as ex:
        print('Error occured : ' + str(ex))

def insert_task(task_id, task_type, labels, project_id):
    return ''

def select_projects():
    select_query = select([PROJECT_TABLE])
    rows = connection.execute(select_query)
    projects = []
    for row in rows:
        projects.append(
            Project(project_id=row['project_id'],
                    project_name=row['project_name'],
                    project_type=row['project_type'],
                    tasks=None))
    return projects