#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:18:56 2020

@author: siddharthsmac
"""

import mysql.connector as sql

connection = sql.connect(
    host = 'localhost',
    user = 'root',
    password = ''
    )

cursor = connection.cursor()
cursor.execute('CREATE DATABASE Siddharth')

cursor.execute('SHOW DATABASES')

for x in cursor:
    print(x)
