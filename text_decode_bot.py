import telebot
import random

token='your_token'
bot=telebot.TeleBot(token)

def crypt(s, key):
    lenKey = len(key)
    start = 0
    p1 = 0
    if (len(s) % lenKey != 0):
        for i in range(lenKey - len(s) % lenKey):
            s += chr(random.randint(ord("!"), ord("=")))

    lenS = len(s)
    sEncrypt = ""

    while (start + lenKey < lenS +1):
        sEncrypt += s[start + key[p1] - 1]
        p1 += 1
        if (p1 == lenKey):
            p1 = 0
            start += lenKey
    return sEncrypt

encryptKey = [3, 6, 4, 2, 1, 5]
decryptKey = [5, 4, 1, 3, 6, 2]

@bot.message_handler(content_types='text')
def start_chat(message):
    bot.send_message(message.chat.id, 'Если хочешь зашифровать свое сообщение то набери текст и отправь последнее сообщение от бота другу. Если хочешь расшифровать то отправь боту зашифрованный текст.')
    stringCrypt = crypt(message.text, encryptKey)
    bot.send_message(message.chat.id, str(stringCrypt))
    stringCrypt = crypt(message.text, decryptKey)
    bot.send_message(message.chat.id, str(stringCrypt))
bot.infinity_polling()
