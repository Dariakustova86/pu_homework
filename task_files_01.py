n = int(input())
p = int(input())

with open('data.txt') as f:
	out1 = ''
	out2 = ''
	for i in f.read().split():
		i = int(i)
		if i%n == 0:
			out1 += str(i) + ' '
		out2 += str(pow(i,p)) + ' '
		
with open('out-1.txt', 'w') as f:
	f.write(out1)

with open('out-2.txt', 'w') as f:
	f.write(out2)
	

