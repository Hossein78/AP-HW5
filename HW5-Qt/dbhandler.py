import sqlite3

conn = sqlite3.connect('mapdb.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    phone integer,
    username text NOT NULL,
    password text NOT NULL)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS locations (
    id integer PRIMARY KEY AUTOINCREMENT,
    user_id integer,
    lat integer,
    lon integer,
    time DATE)
''')

conn.commit()