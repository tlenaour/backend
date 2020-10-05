"""
Add users management
"""

from yoyo import step

__depends__ = {'20200824_01_Utl01-projects-management'}

steps = [
    step("CREATE TABLE platform_user(\
             email text PRIMARY KEY,\
             first_name text ,\
             last_name text,\
             is_deleted boolean);", "DROP  TABLE platform_user;"),
    step("CREATE TABLE role_referential(\
             role varchar(25) PRIMARY KEY);", "DROP  TABLE role_referential;"),
    step("CREATE TABLE user_project_role(\
             project_id varchar(25),\
             email TEXT,\
             role varchar(25),\
             PRIMARY KEY(project_id,email,role),\
             CONSTRAINT fk_project FOREIGN KEY(project_id) REFERENCES project(project_id),\
             CONSTRAINT fk_user FOREIGN KEY(email) REFERENCES platform_user(email),\
             CONSTRAINT fk_role FOREIGN KEY(role) REFERENCES role_referential(role));", "DROP  TABLE user_project_role;")]
