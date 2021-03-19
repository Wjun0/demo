

if __name__ == '__main__':
    import os
    Base_path = os.path.dirname(os.path.abspath(__file__))
    # path = os.path.join(Base_path,'optparse_demo.py')
    # # path = os.path.join(Base_path, 'demo1.py')
    path = os.path.join(Base_path, 'demo2.py')

    os.system(f'python {path} -h')
    # os.system(f'python {path} -H ss')
    # os.system(f'python {path} --port 33')
    os.system(f'python {path} --port 9999 1 2 3')
    os.system(f'python {path} --port 9999')



