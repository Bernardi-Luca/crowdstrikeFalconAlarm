import telepot

def send_message(message):
    token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    bot = telepot.Bot(token)
    number = 00000000000000000000000000
    bot.sendMessage(number, message)
