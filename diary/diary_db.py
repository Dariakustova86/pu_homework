import sqlite3
conn = sqlite3.connect('schema.sql')
cursor = conn.cursor()
sql = '''
	CREATE TABLE IF NOT EXISTS diary (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL DEFAULT,
		task_text TEXT NOT NULL DEFAULT, 
		execution_time NOT NULL DEFAULT
	)
'''
cursor.execute(sql)
conn.commit()
conn.close()
