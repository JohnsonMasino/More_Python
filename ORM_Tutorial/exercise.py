#!/usr/bin/python3

engine.eecute("INSERT INTO employee (emp_name) VALUES (:name)", name='dilbert')
result = engine.execute("SELECT * FROM employee")
result.fetchall()
