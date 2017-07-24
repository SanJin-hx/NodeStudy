'回文联判断'
from functools import *
text = input('请输入一句话:')

def judge(str):
    strfb = reduce(lambda x,y:y+x,str)
    if strfb == str:
        print('{0}是回文联 '.format(str))
    else:
        print('{0}不是回文联 '.format(str))

judge(text)