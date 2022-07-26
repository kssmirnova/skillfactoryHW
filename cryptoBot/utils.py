import requests
import json
from config import currencyKeys

class CcomparatorException(Exception):
    pass

class CryptoCcomparator:
    @staticmethod
    def validateAndGet(currency):
        try:
            return currencyKeys[currency]
        except KeyError:
            raise CcomparatorException(f'Не удалось обработать валюту {currency}')

    @staticmethod
    def getRate(quote, base, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise CcomparatorException(f'Необходимо ввести числовое значение для суммы!')

        quoteKey = CryptoCcomparator.validateAndGet(quote)
        baseKey = CryptoCcomparator.validateAndGet(base)
        if (quoteKey == baseKey):
            raise CcomparatorException('Валюты должны различаться!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quoteKey}&tsyms={baseKey}')
        result = round(json.loads(r.content)[baseKey]*float(amount), 2)
        return result
