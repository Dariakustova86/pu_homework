import time

def pause(s):
	def decorator(func):
		def wrapper(*args, **kwargs):
			time.sleep(s)
			return func(*args, **kwargs)
		return wrapper
	return decorator