a = int(input('Длина списка: '))
b = int(input('Первый член арифметической прогрессии: '))
d = int(input('Знаменатель D геометрической прогрессии '))

spisok = []

for i in range(a):
    spisok.append(b)
    b*=d

print(spisok)
