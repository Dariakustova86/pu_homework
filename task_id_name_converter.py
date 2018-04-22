def camel_to_snake(name):
	newname = ''
	for i in name:
		if i.isupper():
			newname += '_' + i.lower()
		else: newname += i
	if newname[0] == '_':
		newname = newname[1:]
	return newname


def snake_to_camel(name):
	name = name.title().replace('_', '')
	return name
