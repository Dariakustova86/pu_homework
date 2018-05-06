import os.path as Path
import sqlite3

SQL_INSERT_TASK = 'INSERT INTO diary (name, descrip, term) VALUES (?,?,?)'

SQL_UPDATE_TASK_NAME = '''
    UPDATE diary SET name=? WHERE id=?
'''

SQL_UPDATE_TASK_DESCRIP = '''
    UPDATE diary SET descrip=? WHERE id=?
'''

SQL_UPDATE_TASK_TERM = '''
    UPDATE diary SET term=? WHERE id=?
'''

SQL_UPDATE_TASK_SHAPE = '''
    UPDATE diary SET shape=? WHERE id=?
'''

SQL_SELECT_ALL = '''
    SELECT 
        id, name, descrip, term, shape
    FROM 
		diary 
'''

SQL_SELECT_TASK_BY_SHAPE = SQL_SELECT_ALL + ' WHERE shape=?'
SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'
SQL_SELECT_TASK_BY_TERM = SQL_SELECT_ALL + ' WHERE term=?'

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    return conn

def initialize(conn):
    script_path = Path.join(Path.dirname(__file__), 'schema.sql')

    with conn, open(script_path) as f:
        conn.executescript(f.read())
		
def task_all(conn):
	with conn:
		cursor = conn.execute(SQL_SELECT_ALL)
		return cursor.fetchall()

def task_term(conn, term):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_TERM, (term,))
		return cursor.fetchall()

def task_one(conn, id):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (id,))
		return cursor.fetchone()

def task_shape(conn):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_SHAPE, ('Not complete',))
		return cursor.fetchall()

def add(conn, name, descrip, term):
	if not name:
		raise RuntimeError("Task name can't be empty.")
		
	with conn:
		cursor = conn.execute(SQL_INSERT_TASK, (name, descrip, term,))
		pk = cursor.lastrowid
		cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk,))
		return cursor.fetchone()

def update_name(conn, id, name):
	if not name:
		raise RuntimeError("Task name can't be empty.")
		
	with conn:
		conn.execute(SQL_UPDATE_TASK_NAME, (name, id,))
		
def update_descrip(conn, id, descrip):
	with conn:
		conn.execute(SQL_UPDATE_TASK_DESCRIP, (descrip, id,))
			
def update_term(conn, id, term):
	with conn:
		conn.execute(SQL_UPDATE_TASK_TERM, (term, id,))
		
def complete(conn, id):
	with conn:
		conn.execute(SQL_SELECT_TASK_BY_SHAPE, ('Complete', ))
		
def restart(conn, id):
	with conn:
		cursor = conn.execute(SQL_SELECT_TASK_BY_SHAPE, ('Not complete', id,))
		
		
		
		
		
		
		
		
		
		
		
		
		
		

