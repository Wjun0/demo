

#import optparse     # 2.7之后不再更新，建议使用argparse
# parse = optparse.OptionParser()
# parse.add_option('-h',dest='host',default='')
# parse.add_option('-p',dest='port',default='8000')
# (options,args) = parse.parse_args()

# ++++++++++++++++++++++++++++++
#   使用argparse


import argparse
# arg = argparse.ArgumentParser(prefix_chars='-+')  # 不能用默认的配置-，会和系统的冲突，所以用prefix_chars 指定
arg = argparse.ArgumentParser()  # 不能用默认的配置-，会和系统的冲突，所以用prefix_chars 指定
# arg.add_argument('+h','--host',dest='host',default='my_host')
# arg.add_argument('+p','--port',dest='port',type=str, default='my_port')

arg.add_argument('-H','--host',dest='host',default='my_host')     # 不能使用-h 和系统的冲突
arg.add_argument('-p','--port',dest='port',type=str, default='my_port')
arg.add_argument()
opt = arg.parse_args()


def optparse_test():
    print('===================')
    print("port:"+ opt.port)
    print("host:"+ opt.host)



if __name__ == '__main__':
    optparse_test()