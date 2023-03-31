import random

class Password():
    while True:
        print('\nЗдравствуйте. Добро пожаловать в генератор паролей. С каких символов вы хотите пароль?')
        password = input()
        print('Введите длину пароля')
        length = int(input())
        characters = list('abcdefghijklmnopqrstuvwxyz')
        if password == 'верхний регистр':
            characters.extend(list('ABCDEFGIJKLMNOPQRSTUVWXYZ'))
        if password == 'спец символы':
            characters.extend(list('!@#$%^&*()'))
        if password == 'цифры':
            characters.extend(list('0123456789'))
        if password == 'цифры и верхний регистр':
            characters.extend(list('0123456789ABCDEFGIJKLMNOPQRSTUVWXYZ'))
        if password == 'цифры и спец символы':
            characters.extend(list('!@#$%^&*()0123456789'))
        if password == 'верхний регистр и спец символы':
            characters.extend(list('ABCDEFGIJKLMNOPQRSTUVWXYZ!@#$%^&*()'))
        thepassword = ''
        for x in range(length):
            thepassword += random.choice(characters)
        print(thepassword)

password = Password()
print(password)


