def average(lst):
	element = lst[0]
	for index in range(len(lst)-1):
		index += 1
		element += lst[index]
	return round(element / (index + 1), 3)



