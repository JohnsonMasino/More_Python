#!/usr/bin/python3
from sqlalchemy import Integer, String, Datetime

eng = engine.("sqlite://")
Table1 = Tabale('network', 'MetaData',
        Column('network_id', integer, primary_key=True),
        Column('name', String(100), nullable=False),
        Column('created_at', DateTime, nullable=False),
        Column('owner_id', Integer foreign_key('user.id')))
metadata.create_all(engine)
