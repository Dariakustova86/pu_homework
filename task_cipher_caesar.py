
def encode(text, n=0):
	newtext = ''
	for i in range(len(text)):
		number = ord(text[i])
		if number >= 65 and number <= 90 or number >= 97 and number <= 122:
			number = number + n
			if text[i].isupper():
				if number > ord('Z'):
					number -= 26
			elif number > ord('z'):
				number -= 26
			letter = chr(number)
			newtext += letter
		elif number > 0 and number < 65 or number > 90 and number < 97 or number > 122:
			symletter = chr(number)
			newtext += symletter
	return newtext	
		
def decode(text, n=0):
	newtext = ''
	for i in range(len(text)):
		number = ord(text[i])
		if number >= 65 and number <= 90 or number >= 97 and number <= 122:
			number = number - n
			if text[i].isupper():
				if number < ord('A'):
					number += 26
			elif number < ord('a'):
				number += 26
			letter = chr(number)
			newtext += letter
		elif number > 0 and number < 65 or number > 90 and number < 97 or number > 122:
			symletter = chr(number)
			newtext += symletter
	return newtext

