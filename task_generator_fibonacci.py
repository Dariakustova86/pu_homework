def fibonacci(n):
	f1 = 1
	f2 = 1
	yield 1
	yield 1
	
	for i in range(2, n):
		f = f1 + f2
		f1 = f2
		f2 = f
		yield f

	