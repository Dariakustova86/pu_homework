def login_required(func):
	def wrapper(*args, **kwargs):
		def token_txt(read):
			with open('token.txt') as f:
				read = f.read()
		for i in range(3):
			username = input()
			password = input()
			test = make_token(token_txt(username, password))
			if test == True:
				break
			return read 
		return func(*args, **kwargs) if test else None
	return wrapper