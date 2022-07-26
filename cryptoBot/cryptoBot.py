import telebot
from config import currencyKeys, TOKEN
from utils import CryptoCcomparator, CcomparatorException


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message):
    help = "Привет! Это конвертор валют.\n" \
           "Вы можете посмотреть доступный список валюят по команде /values \n" \
           "Все просто: чтобы получить курс введите \n" \
           "<Целевую валюту> <Вашу валюту> <Сумма>"
    bot.send_message(message.chat.id, help)

@bot.message_handler(commands=['values'])
def values(message):
    values = "Список доступных валют"
    for key in currencyKeys.keys():
        values = '\n'.join((values, key))
    bot.reply_to(message, values)


@bot.message_handler(content_types=['text'])
def getRate(message):
    try:
        params = message.text.split(' ')
        if (len(params) > 3):
            raise CcomparatorException("Слишком много аргументов")
        if (len(params) < 3):
            raise CcomparatorException("Слишком мало аргументов")
        quote, base, amount = params

        result = CryptoCcomparator.getRate(quote, base, amount)
        resultMessage = f'Цена за {amount} {quote} - {result} {base}'

    except CcomparatorException as e:
        bot.send_message(message.chat.id, str(e) + '\nПрочитать инструкцию /help')
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Не удалось обработать команду, произошла системная ошибка')
    else:
        bot.send_message(message.chat.id, resultMessage)


bot.polling(none_stop=True)
