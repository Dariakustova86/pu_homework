import hashlib

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()
	
user_aut == False

def login_required(func):
    def wrapper(*args, **kwargs):
        global user_aut
        if user_aut == False:
            i = 0
            while i < 3 :
                user = input()
                password = input()
                with open('token.txt') as token:
                    if make_token(user, password) != token.read():
                        i += 1
                    else:
                        user_aut == True
                        return func(*args, **kwargs)
            return None
        else:
            return func(*args, **kwargs)
    return wrapper