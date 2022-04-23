a = int(input('Длина списка: '))

spisok = [1, 1]

for i in range(a-2):
    spisok.append(spisok[len(spisok)-1]+spisok[len(spisok)-2])

print(spisok)
