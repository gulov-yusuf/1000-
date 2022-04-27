a = int(input('Длина списка: '))

spisok = []
spisok_chetnih = []

for i in range(a):
    c = int(input('Что добавить в список: '))
    spisok.append(c)


for i in spisok:
    if (i%2==0):
        spisok_chetnih.append(i)

spisok_chetnih = spisok_chetnih[::-1]

for z in spisok_chetnih:
    print(z, end = ', ')

print('')
print(f'Количество чётных чисел в списке: {len(spisok_chetnih)}')
