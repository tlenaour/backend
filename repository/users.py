from sqlalchemy import select, join
from config.database import metadata, connection
from domain.users import User, UserProjectRole
from repository.project import PROJECT_TABLE
USERS_TABLE_NAME = 'platform_user'
USER_PROJECT_ROLE_TABLE_NAME = 'user_project_role'
ROLE_REFERENTIAL_TABLE_NAME = 'role_referential'

USERS_TABLE = metadata.tables[USERS_TABLE_NAME]
USER_PROJECT_ROLE_TABLE = metadata.tables[USER_PROJECT_ROLE_TABLE_NAME]
ROLE_REFERENTIAL_TABLE = metadata.tables[ROLE_REFERENTIAL_TABLE_NAME]


def select_users():
    select_query = select([USERS_TABLE]).where(USERS_TABLE.c.is_delete is False)
    rows = connection.execute(select_query)
    users = []
    for row in rows:
        users.append(User(email=row['email'],
                          first_name=row['first_name'],
                          last_name=row['last_name']))
    return users


def select_projects_roles_by_user(email):
    join_tables = USERS_TABLE.join(USER_PROJECT_ROLE_TABLE, USERS_TABLE.c.email == USER_PROJECT_ROLE_TABLE.c.email)
    query = select([USER_PROJECT_ROLE_TABLE.c.email, USER_PROJECT_ROLE_TABLE.c.project_id, USER_PROJECT_ROLE_TABLE.c.role]).select_from(join_tables).where(USER_PROJECT_ROLE_TABLE.c.email == email)
    rows = connection.execute(query)
    users = []
    for row in rows:
        users.append(UserProjectRole(email=row['email'],
                              project_id=row['project_id'],
                              role=row['role']))
    return users


def select_roles_referential():
    select_query = select([ROLE_REFERENTIAL_TABLE])
    rows = connection.execute(select_query)
    roles = []
    for row in rows:
        roles.append(row['role'])
    return roles


def insert_role_to_referential(role):
    insert = ROLE_REFERENTIAL_TABLE.insert().values(role=role)
    try:
        result = connection.execute(insert)
    except Exception as ex:
        print('Error occured : ' + str(ex))


def insert_user(email, last_name, first_name):
    insert = USERS_TABLE.insert().values(email=email,
                                         last_name=last_name,
                                         first_name=first_name,
                                         is_deleted=False)
    try:
        result = connection.execute(insert)
    except Exception as ex:
        print('Error occured : ' + str(ex))


def insert_role_for_user(email, project_id, role):
    insert = USER_PROJECT_ROLE_TABLE.insert().values(email=email,
                                                     project_id=project_id,
                                                     role=role)
    try:
        result = connection.execute(insert)
    except Exception as ex:
        print('Error occured : ' + str(ex))