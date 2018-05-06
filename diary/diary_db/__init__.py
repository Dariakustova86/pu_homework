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
	with get_connection() as conn:
		if not storage.task_one(conn, id):
			print('Попробуй ввести правильный номер')
		return 
	
	def redact_task_name():
		with get_connection() as conn:
			update_name = input('\nПереименуй задачу: ')
			storage.update_name(conn, id, update_name)
		return 0
		
	def redact_task_descrip():
		with get_connection() as conn:
			update_descript= input('\nПерепиши описание: ')
			storage.update_task_descrip(conn, id, update_descrip)
		return 0
		
	def redact_task_time():
		with get_connection() as conn:
			update_time = input('\nПрокрастинируем. Введи дату в виде «YYYY.MM.DD»: ')
			storage.update_term(conn, id, update_term)
		return 0
		
		
	def redact_show_menu():
		print('''Режим редактирования. Выберите действие:
	1. Изменить название задачи
	2. Изменить описание
	3. Изменить дату
	''')
		edit_actions = {
			'1': redact_task_name,
			'2': redact_task_descrip,
			'3': redact_task_time,
		}
		while 1: 
			redact_show_menu()
			cmd = input('\nВведите команду: ')
			action = edit_actions.get(cmd)
			if action:
				action()
			else:
				print('Не известная команда')
			
def tasks_complete():
	id = input('\nНомер задачи: ')
	with get_connection() as conn:
		if not storage.task_one(conn, id):
			print('Попробуй ввести правильный номер')
		else:
			storage.complete(conn, id)
			
def tasks_restart():
	id = input('\nНомер задачи: ')
	with get_connection() as conn:
		if not storage.task_one(conn, id):
			print('Попробуй ввести правильный номер')
		else:
			storage.restart(conn, id)
			
def tasks_show_menu():
	print(''' Ежедневник прокрастинатора. Выберите действие:
1. Добавить задачу 
2. Редактировать задачу 
3. Заверщить задачу
4. Начать задачу сначала 
5. Вывести список задач
6. Вывести список задач по дате 
7. Вывести список невыполненных задач
m. Показать меню
q. Выйти
''')

def go_away():
	sys.exit(0)

def main():
	tasks_show_menu()
	actions = {
		'1': tasks_add,
		'2': tasks_edit,
		'3': tasks_complete,
		'4': tasks_restart,
		'5': tasks,
		'6': tasks_term,
		'7': tasks_not_complete,
		'm': tasks_show_menu,
		'q': go_away,
	}
	while 1: 
		cmd = input('\nВведите команду: ')
		action = actions.get(cmd)
		
		if action:
			action()
		else:
			print('Не известная команда')
	