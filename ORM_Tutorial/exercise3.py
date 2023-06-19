#!/usr/bin/python3

"""
1. Create a class/mapping for this table. call it Network.

CREATE TABLE network (
    network.id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
)

2. emit Base.metadata.create_all(engine) to create the table

3. commit a few network objects to the database:
    Network(name="net1"), Network(name="net2")
"""

class Network(Base):
    """defines the class of the table"""
    __tablename__ = "Network"
    network_id = Column(Integer, primanry_key=True)
    name = Column(String(100), nullable=False)

Base.metadata.create_all(engine)

session.add_all([Network(name="net1"), Network(name="net2")])

session.flush()
