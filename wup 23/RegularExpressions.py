import re

def validateEmail(address):
    if re.search(pattern = '[a-zA-Z]+@[a-zA-Z]+\.[a-z]+', string = address) != None:
        return True
    else:
        return False

def validateDate(date):
    if re.search(pattern = '[1-3]?[0-9]/1?[0-9]/[1-9]+', string = date) != None:
        return True
    else:
        return False

print(validateEmail(r'testTest@gmail.com'))

print(validateDate(r'1/23/2000'))
    
