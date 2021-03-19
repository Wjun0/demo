
# 将命令行的参数 和
# command: python dem01.py 8 2 --sum
# 结果：10

# command : python dem01.py 1 2 3 4
# 结果：4  找最大的一个

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args)
print(args.integers)
print(args.accumulate(args.integers))


