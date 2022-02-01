per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Сумма вклада: ")

deposit = []
deposit.append(per_cent.get('ТКБ') * float(money) / 100)
deposit.append(per_cent.get('СКБ') * float(money) / 100)
deposit.append(per_cent.get('ВТБ') * float(money) / 100)
deposit.append(per_cent.get('СБЕР') * float(money) / 100)
deposit = list(map(int, deposit))

print(deposit)
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))
