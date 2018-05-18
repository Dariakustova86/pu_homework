def get_free_land(station, garden_bed):
	w = garden_bed[0]
	s = garden_bed[1]
	square_bed = w * s
	if station[0] == 0:
		raise ValueError('Не задана площадь участка')
	if garden_bed[0] == 0 or garden_bed[1] == 0:
		raise ValueError('Не задана площадь грядки')
	if square_bed > station[0] * 100:
		raise ValueError('Размер грядки больше размера участка')
	return station[0] * 100 % square_bed
	


		
	