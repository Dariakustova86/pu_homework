def is_palindrome(s):
	s = str(s)
	sdel = s.lower().replace(' ','')
	srev = sdel[::-1]
	if sdel != srev:
		return False
	return True
