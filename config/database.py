from sqlalchemy import create_engine, MetaData, inspect
import os

db_uri = 'postgresql://annotation_platform:azerty@localhost:5432/annotations'

try:
    engine = create_engine(db_uri)
    print('Successfully create engine')
except Exception as ex:
    print('Error create engine : '+ex.__str__())

try:
    connection = engine.connect()
    print('Successfully create connection')
except Exception as ex:
    print('Error create connection : '+ex.__str__())

metadata = MetaData(engine, reflect=True)
inspector = inspect(engine)

