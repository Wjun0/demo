import sys
import os


basepath = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0,basepath)
print(basepath)
from log import Logger


if __name__ == '__main__':
    log = Logger('all_log',level='debug')
    log.logger.error('error')
    log.logger.info('info')

    # this dev
    # this is debug
    # debug ok
    # dev ok


