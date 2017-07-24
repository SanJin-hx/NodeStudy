def bin(x):
    result = ''
    temp = []
    while x!=0:
        y = int(x%2)
        x = int(x/2)
        temp.append(y)
    while temp:
        result += str(temp.pop())
    return result
x = int(input('请输入一个整数:'))

print(bin(x))