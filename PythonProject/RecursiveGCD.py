x = int(input('请输入一个整数:'))
y = int(input('请输入一个整数:'))

def Gcd(x,y):
    if y:
        return Gcd(y,x%y)
    else:
        return x

print(Gcd(x,y))