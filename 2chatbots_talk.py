from cleverbot import Cleverbot
import jtalk
bot1 = Cleverbot()
bot2 = Cleverbot()

text = '私はロボットです'
print('bot2 >> {}'.format(text))
jtalk.jtalk(text)

while True:
    text = bot1.ask(text).encode('ISO-8859-1').decode('utf-8')
    print('bot1 >> {}'.format(text))
    jtalk.jtalk(text, voice='tohoku')
    text = bot2.ask(text).encode('ISO-8859-1').decode('utf-8')
    print('bot2 >> {}'.format(text))
    jtalk.jtalk(text)

