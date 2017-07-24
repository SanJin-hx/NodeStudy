import sys

num = input('请输入一个整数(输入Q结束程序):')

def numhex(x):
    y = hex(x)
    print('十进制-->十六进制:',x)

def numoct(x):
    y = oct(x)
    print('十进制-->八进制:',y)

def numbin(x):
    y = bin(x)
    print('十进制-->二进制:',y)

def judge(x):
    if(x == 'Q'):
        sys.exit(0)
    else:
        x = int(x)
        numhex(x)
        numoct(x)
        numbin(x)
judge(num)        

