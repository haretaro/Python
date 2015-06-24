import sys
import termios
import tty

fd = sys.stdin.fileno()

print('push any key')
old_settings = termios.tcgetattr(fd)
try:
    tty.setraw(fd)
    ch = sys.stdin.read(1)
finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
print(ch)
