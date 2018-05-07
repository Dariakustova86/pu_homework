import sys

from diary_db import storage
get_connection = lambda: storage.connect('diary.sqlite')

def tasks():
	with get_connection() as conn:
		print(storage.task_all(conn))
		
def tasks_term():
	term = input('\nСегодня ты ничего не делал. Введи дату в виде «YYYY.MM.DD»: ')
	with get_connection() as conn:
		print(storage.task_term(conn, term))
		
def tasks_not_complete():
	with get_connection() as conn:
		print(storage.task_shape(conn))
		
def tasks_add():
	name = input('\nКакую задачу записать и забыть?: ')
	descrip = input('\nНемножко о задаче: ')
	term = input('\nБудь оптимистом. Напиши дату выполнения в виде «YYYY.MM.DD»: ')
	with get_connection() as conn:
		print(storage.add(conn, name, descrip, term))
		
def tasks_edit():
	id = input('\nПомнишь номер задачи?: ')
	print('''Режим редактирования. Выберите действие:
	1. Изменить название задачи
	2. Изменить описание
	3. Изменить дату
	4. Изменить статус задачи
	5. Выход из режима редактирования
	''')		
	
	with get_connection() as conn:
		if not storage.task_one(conn, id):
			print('Попробуй ввести правильный номер')		
	
	def redact_task_name():
		with get_connection() as conn:
			update_name = input('\nПереименуй задачу: ')
			storage.update_name(conn, id, update_name)
		
		
	def redact_task_descrip():
		with get_connection() as conn:
			update_descrip= input('\nПерепиши описание: ')
			storage.update_descrip(conn, id, update_descrip)
		
		
	def redact_task_time():
		with get_connection() as conn:
			update_term = input('\nПрокрастинируем. Введи новую дату в виде «YYYY.MM.DD»: ')
			storage.update_term(conn, id, update_term)
			
	def redact_task_complete():
		with get_connection() as conn:
			shape = input('\nИзменить статус задачи: ')
			storage.complete(conn, id, shape)
	
		
	edit_actions = {
		'1': redact_task_name,
		'2': redact_task_descrip,
		'3': redact_task_time,
		'4': redact_task_complete,
		'5': main,
	}
	
	while 1:
		cmd = input('\nВведите команду: ')
		action = edit_actions.get(cmd)
		if action:
			action()
		else:
			print('Неизвестная команда')
			
			
def tasks_restart():
	id = input('\nВсе еще помнищь номер задачи?: ')
	with get_connection() as conn:
		if not storage.task_one(conn, id):
			print('Попробуй ввести правильный номер')
		else:
			storage.restart(conn, id)
			
def tasks_show_menu():
	print(''' Ежедневник прокрастинатора. Выберите действие:
1. Добавить задачу 
2. Редактировать задачу
3. Начать задачу сначала 
4. Вывести список задач
5. Вывести список задач по дате 
6. Вывести список невыполненных задач
m. Показать меню
q. Выйти
''')

def go_away():
	sys.exit(0)

def main():
	with get_connection() as conn:
		storage.initialize(conn)
	tasks_show_menu()
	actions = {
		'1': tasks_add,
		'2': tasks_edit,
		'3': tasks_restart,
		'4': tasks,
		'5': tasks_term,
		'6': tasks_not_complete,
		'm': tasks_show_menu,
		'q': go_away,
	}
	while 1: 
		cmd = input('\nВведите команду: ')
		action = actions.get(cmd)
		
		if action:
			action()
		else:
			print('Неизвестная команда')
	