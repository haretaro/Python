import sys
list = []
while True:
    input = sys.stdin.readline()
    if input=="\n":
        break
    list.append(int(input))
print(list)
