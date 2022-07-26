import requests

# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html') # делаем запрос на сервер по переданному адресу

# print(r.content)
# print(r.status_code) # узнаем статус полученного ответа

# import requests
import json  # импортируем необходимую библиотеку

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
# print(type(texts))  # проверяем тип сконвертированных данных
#
# for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
#     print(text[:50], '\n')



# import requests

r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
print(json.loads(r.content)['USD'])


# myFile = open('D:\Desktop\Дом Питомца\el.txt', 'rt', encoding="utf8")
# print(myFile.read())

# round(n / math.log(n, 2))