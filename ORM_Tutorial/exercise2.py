#!/usr/bin/python3
from sqlalchemy import Inspector, Reflector

network_reflected = Table('network', metadata2, autolaod=True, autolaod_with(engine))
network_reflected

for tname in inspector.get_table_names():
    for column in inspector.get_columns(tname):
        if column['name'] == story_id:
            print(tname)
