a = int(input('Длина списка: '))

spisok = []

for i in range(a):
    c = input('Что добавить в список: ')
    spisok.append(c)

print(spisok[::-1])
