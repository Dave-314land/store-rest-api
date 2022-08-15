import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

create_table_users = "CREATE TABLE if not exists users (id INTEGER PRIMARY KEY, username text, password text)"
create_table_items = "CREATE TABLE if not exists items (id INTEGER PRIMARY KEY, item_name text, price real)"

cur.execute(create_table_users)
cur.execute(create_table_items)

con.commit()
con.close()