import hashlib

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()

user_aut = False

def login_required(func):
    def wrapper(*args, **kwargs):
        global user_aut
        with open('token.txt') as f:
            token = f.read()
        i = 3
        if user_aut == False:
            while i:
                user = input()
                password = input()
                up = make_token(user, password)
                if up == token:
                    user_aut = True
                    return func(*args, **kwargs)
                else:
                    i -= 1
        return func(*args, **kwargs) if user_aut == True else None
    return wrapper
			