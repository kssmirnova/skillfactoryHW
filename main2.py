S = 0
n = int(input('Количество билетов: '))
for i in range(1,n+1):
    print('Введите возраст', i, '-го посетителя: ')
    a = int(input())
    if a < 18:
        S += 0
    if 18 <= a < 25:
        S = S + 990
    if a >= 25:
        S += 1390

if n > 3:
    S = int(0.9 * S)

print('Сумма:', S, 'рублей')
