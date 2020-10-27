#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:12:38 2020

@author: siddharthsmac
"""

import mysql.connector as sql

connection = sql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'Siddharth'
    )

cursor = connection.cursor()
cursor.execute('CREATE TABLE studentinfo (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), subject VARCHAR(255))')

query = 'INSERT INTO studentinfo (name, subject) VALUES (%s, %s)'

values = ('John', 'stats')

cursor.execute(query, values)
cursor.execute('select * from studentinfo')
print(cursor.fetchall())

query = 'INSERT INTO studentinfo (name, subject) VALUES (%s, %s)'

value = [('Siddharth', 'stats'),
          ('Joe', 'maths'),
          ('Ankur', 'Data science'),
          ('Paul', 'Data science'),
          ('Vishal', 'maths'),
          ('Sid', 'Data science')]

cursor.executemany(query, value)
print('Row inserted', cursor.lastrowid)

cursor.execute('select * from studentinfo')

lst = cursor.fetchall()

for records in lst:
    print(records)
    
cursor.execute("select * from studentinfo where name = 'Sid'")
print(cursor.fetchall())

cursor.execute('select subject from studentinfo')
print(cursor.fetchall())

cursor.execute('select distinct subject from studentinfo')
print(cursor.fetchall())

cursor.execute("SELECT name, subject FROM studentinfo where name = 'Sid' or subject = 'Data science'")
print(cursor.fetchall())



cursor.execute('DROP TABLE studentinfo')
