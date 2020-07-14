'''
 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка
'''

my_note = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_note.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_note.close()
my_note = open('test.txt', 'r')
content = my_note.readlines()
print(content)
my_note.close()
