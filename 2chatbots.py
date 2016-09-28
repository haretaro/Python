from cleverbot import Cleverbot
bot1 = Cleverbot()
bot2 = Cleverbot()

text = 'こんにちは'
while True:
    text = bot1.ask(text).encode('ISO-8859-1').decode('utf-8')
    print('bot1 >> {}'.format(text))
    text = bot2.ask(text).encode('ISO-8859-1').decode('utf-8')
    print('bot2 >> {}'.format(text))

