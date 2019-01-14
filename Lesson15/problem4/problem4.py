print('-'*60)

password = input('What is the password?: ')

while password not in ['Open Sesame']:
	password = input('Password is invaid, try again: ')

print('Password is valid! Welcome!!')


print('-'*60)