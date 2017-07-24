def gcd(x,y):
    return x if y == 0 else gcd(y,x%y)

x = int(input('请输入一个整数:'))
y = int(input('请输入一个整数:'))

print(gcd(x,y))