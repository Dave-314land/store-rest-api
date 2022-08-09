import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

create_table = "CREATE TABLE if not exists users (id INTEGER PRIMARY KEY, username text, password text)"
cur.execute(create_table)

con.commit()
con.close()