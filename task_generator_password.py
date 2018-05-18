import random
import string

def password_generator(n):
    while 1:
        password = ''
        for i in range(n):
            password += random.choice(string.ascii_letters)
        yield password

		
		
			
		
		
