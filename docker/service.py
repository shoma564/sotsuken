#import aa

def check_string():
    with open('temp.txt') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'blabla' in line:
            return True # The string is found
    return False  # The string does not exist in the file

if check_string():
    print('True')
else:
    print('False')
