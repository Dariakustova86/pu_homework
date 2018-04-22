def bubble_sort(lst):
	n = 1 
	while n < len(lst): #внешний цикл устанавливает количество проходов по списку (количество итераций: n-1)
		for index in range(len(lst)-n): #вложенный цикл сравнивает соседние элементы и при необходимости меняет их местами. количество сравнений каждый раз уменьшается на n
			if lst[index] > lst[index+1]: #сравнение элементов
				lst[index],lst[index+1] = lst[index+1],lst[index] #элементы меняются местами
		n += 1 
	return lst

	
lst = bubble_sort(1, 78, 98, 4, 2, 67)