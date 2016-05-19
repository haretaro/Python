import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', type=int, help='display a square of given number')
parser.add_argument('-n', '--num', type=int, default=1, help='number of iteration')
parser.add_argument('-f', '--flag', help='falg', action='store_true')
args = parser.parse_args()
if args.flag:
    print('verbverb')
for i in range(args.num):
    print(args.square ** 2)
