plates = int(input())
detergent = int(input())
if plates == detergent / 0.5:
	print('Все тарелки вымыты, моющее средство закончилось')
elif plates > detergent / 0.5:
	print('Моющее средство закончилось. Осталось', plates - int(detergent / 0.5), 'тарелок')
elif plates < detergent / 0.5:
	print('Все тарелки вымыты. Осталось', detergent - plates * 0.5, 'ед. моющего средства')
