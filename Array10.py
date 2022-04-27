a = int(input('Длина списка: '))

spisok = []
spisok_chetnih = []
spisok_nechetnih = []

for i in range(a):
    c = int(input('Что добавить в список: '))
    spisok.append(c)


for i in spisok:
    if (i%2==0):
        spisok_chetnih.append(i)
    elif (i%2==1):
        spisok_nechetnih.append(i)

spisok_nechetnih = spisok_nechetnih[::-1]

for z in spisok_chetnih:
    print(z, end = ', ')

print('')

for z in spisok_nechetnih:
    print(z, end = ', ')
