a = int(input('Длина списка: '))

spisok = []
spisok_nechetnih = []

for i in range(a):
    c = int(input('Что добавить в список: '))
    spisok.append(c)


for i in spisok:
    if (i%2==1):
        spisok_nechetnih.append(i)

for z in spisok_nechetnih:
    print(z, end = ', ')

print('')
print(f'Количество нечётных чисел в списке: {len(spisok_nechetnih)}')
