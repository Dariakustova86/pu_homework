def tasks():
	print('Список задач, которые ты может быть сделаешь')
def add():
	print('Добавить задачу, которую ты не сделаешь')
def edit():
	print('Отредактируй задачу, которую не хочешь делать')
def complete():
	print('Выполненные задачи. Очень смешно')
def restart():
	print('Начни ничего не делать сначала')
def go_away():
	print('"У" - уходи')
	
	
print('''
Ежедневник прокрастинатора. Выберите действие:

1. Вывести список задач 
2. Добавить задачу 
3. Отредактировать задачу 
4. Заверщить задачу
5. Начать задачу сначала 
6. Выход
''')


def func_menu(num):
	if num == 1:
		tasks()
		return True
	elif num == 2:
		add()
		return True
	elif num == 3:
		edit()
		return True
	elif num == 4:
		complete()
		return True
	elif num == 5:
		restart()
		return True
	elif num == 6:
		go_away()
		return False
	else:
		print('Введите число от 1 до 6')
		return True
		
		
cycle_stop = True
while cycle_stop:
	num = int(input('Введите число: '))
	cycle_stop = func_menu(num)
	
	
	
	
	
	
	
	
	
