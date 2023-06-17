#!/usr/bin/python3

"""creates a connection using an in-memory-only SQLite database"""

from sqlalchemy import create_engine as cr
engine = cr('sqlite:///:memory:', echo=True)
