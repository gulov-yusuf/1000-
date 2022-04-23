a = int(input('Длина списка: '))

spisok = []

s = 1

for i in range(a):
    spisok.append(2**s)
    s+=1

print(spisok)
