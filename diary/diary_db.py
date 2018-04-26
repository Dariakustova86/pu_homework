import sqlite3
conn = sqlite3.connect('schema.sql')
cursor = conn.cursor()
sql = '''
	CREATE TABLE IF NOT EXISTS diary (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name NOT NULL,
		task_text NOT NULL,
		time NOT NULL
	)
'''
cursor.execute(sql)
conn.commit()
conn.close()