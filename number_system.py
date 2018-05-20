def number_system(num, sys):
    result=''
    hex1 = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    while num % sys or num // sys:
        if num % sys in hex1.keys():
            result += str(hex1[num % sys])
        else:
            result += str(num % sys)
        num = num // sys
    return result[::-1]
	
def number_system_dec(num, sys):
    num = str(num)
    num = num[::-1]
    hex2 = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    co=0
    su=0
    for i in num:
        if i in hex2.keys():
            i = hex2[i]
        su +=int(i) * sys ** co
        co += 1
    return su
	
def dec2bin(number):
    return number_system(number,2)
def dec2oct(number):
    return number_system(number,8)
def dec2hex(number):
    return number_system(number,16)
	
def bin2dec(number):
    return number_system_dec(number,2)
def oct2dec(number):
    return number_system_dec(number,8)
def hex2dec(number):
    return number_system_dec(number,16)