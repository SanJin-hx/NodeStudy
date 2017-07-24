def Daffoild(x,base=3):
    num = x
    result = 0
    x = list(str(x))
    for y in x:
        result += int(y)**base
    if num == result:
        print('{0}是水仙花数'.format(num))
    else:
        print('{0}不是水仙花数'.format(num))

Daffoild(111)