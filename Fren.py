import telebot
from conf import keys, TOKEN
from extensions import conventor, convertionException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def star(message: telebot.types.Message):
    text2 = f"привет, {message.chat.username}, напиши /help чтобы узнать что нужно делать"
    bot.reply_to(message, text2)
    print(message.text)


@bot.message_handler(commands=['help'])
def help_(message: telebot.types.Message):
    text = "введите команду боту в следующем формате \n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \n\nувидеть список всех доступных валют /values"
    bot.reply_to(message, text)
    print(message.text)


@bot.message_handler(commands=['values'])
def valu(message: telebot.types.Message):
    text3 = 'доступные валюты'
    for key in keys:
        text3 = '\n'.join((text3, key,))
    bot.reply_to(message, text3)
    print(message.text)


@bot.message_handler(content_types=['photo'])
def nice(message):
    bot.reply_to(message, 'миленько')


@bot.message_handler(content_types=['text'])
def content(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise convertionException('слишком много параметров или слишком мало')
        quote, base, amaout = values
        result = conventor.get_price(quote, base, amaout)
    except convertionException as e:
        bot.reply_to(message, f'где то есть косяк, попробуйте ещё разок\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'не удалось обработать команду\n проблема с сервером(\n{e}')
    else:
        text4 = f'цена {amaout} {quote} в {base} - {result}'
        bot.reply_to(message, text4)
    print(message.text)


bot.polling()
