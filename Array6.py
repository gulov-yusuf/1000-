a = int(input('Длина списка: '))
A = int(input('А: '))
B = int(input('B: '))

spisok = [A, B]

for i in range(a-2):
    spisok.append(sum(spisok))

print(spisok)
