from collections import namedtuple


def return_namedtuple(*name):
	def decorator(func):
		def wrapper(*args, **kwargs):
			original = func(*args, **kwargs)
			if isinstance(original, tuple):
				new = namedtuple('new', list(name))
			return new(*original)
		return wrapper
	return decorator
	