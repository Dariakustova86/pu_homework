x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
vecx1 = x2 - x1
vecy1 = y2 - y1
vecx2 = x3 - x2
vecy2 = y3 - y2
vecx3 = x1 - x3
vecy3 = y1 - y3
sk1 = vecx1 * vecx2 + vecy1 * vecy2
sk2 = vecx2 * vecx3 + vecy2 * vecy3
sk3 = vecx1 * vecx3 + vecy1 * vecy3
if sk1 == 0 or sk2 == 0 or sk3 == 0:
	print('yes')
else:
	print('no')
