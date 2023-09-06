string = str(input('Enter a string of more than 6 characters: '))
while len(string) < 6:
    string = str(input('enter a string of more than 6 characters again: '))
new_str = string[-5:]
print('Result: ', new_str)