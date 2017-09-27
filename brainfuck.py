import sys

source = None
if len(sys.argv) > 1:
    source_file = sys.argv[1]
    source = open(source_file)

memory = [0]
pointer = 0
reader = 0
bracket = {}
debug = False

def color_memory():
    c = [str(x) for x in memory]
    c[pointer] = '\033[92m' + c[pointer] + '\033[0m'
    return '[' + ', '.join(c) + ']'

def check_bracket(program):
    global bracket
    stack = []
    for i in range(len(program)):
        if program[i] == '[':
            stack.append(i)
        if program[i] == ']':
            rb = stack.pop()
            bracket[i] = rb
            bracket[rb] = i

def rshift():
    global pointer
    pointer += 1
    if len(memory) <= pointer:
        memory.append(0)
    return reader + 1

def lshift():
    global pointer
    pointer -= 1
    if pointer < 0:
        raise('Pointer less than 0')
    return reader + 1

def plus():
    memory[pointer] += 1
    return reader + 1

def minus():
    memory[pointer] -= 1
    return reader + 1

def printout():
    print(chr(memory[pointer]), end='')
    return reader + 1

def getinput():
    memory[pointer] = ord(input()[0])
    return reader + 1


def rbracket():
    if memory[pointer] != 0:
        return bracket[reader] + 1
    else:
        return reader + 1

def lbracket():
    if memory[pointer] == 0:
        return bracket[reader] + 1
    else:
        return reader + 1

def enable_debug():
    global debug
    debug = True
    return reader + 1

op = {'>': rshift,
        '<': lshift,
        '+': plus,
        '-': minus,
        '.': printout,
        ',': getinput,
        '[': lbracket,
        ']': rbracket,
        'D': enable_debug
        }

program = ',.' if source is None else source.read()

check_bracket(program)
while reader < len(program):
    if program[reader] in op:
        if debug is True:
            print(program[reader], color_memory())
        reader = op[program[reader]]()
    else:
        reader += 1

print('')
if source is not None:
    source.close()
