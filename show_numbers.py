import sys
import termios
import tty
import select
import time

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

n=1
while True:
    print(n)
    n += 1

    try:
        tty.setraw(fd,termios.TCSANOW)
        if sys.stdin in select.select([sys.stdin],[],[],0)[0]:
            print(sys.stdin.read(1))
            break
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
    
    time.sleep(0.1)
