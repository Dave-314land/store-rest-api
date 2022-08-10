import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

create_table_users = "CREATE TABLE if not exists users (id INTEGER PRIMARY KEY, username text, password text)"
create_table_items = "CREATE TABLE if not exists items (item_name text, price real)"

cur.execute(create_table_users)
cur.execute(create_table_items)

# Test data - delete later
cur.execute("INSERT INTO items VALUES ('test_item', 10.99)")

con.commit()
con.close()