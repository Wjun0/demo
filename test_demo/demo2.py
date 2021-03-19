
# 可以接收位置参数和指定参数

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', type=int, nargs='*',help='an integer for the accumulator')  # 接收位置参数，放到列表中
parser.add_argument('-p','--port',dest='port',type=str, default='my_port')          # 接收指定参数，放到对象中

args = parser.parse_args()
print(args)
print(args.integers)

