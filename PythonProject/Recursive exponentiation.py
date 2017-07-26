num = int(input('请输入一个整数:'))
ToThePower = int(input('请输入次方数:'))
def power(x,y):
    result = x
    if y==1:
        return 1
    else:
        result *= power(x,y-1)
    return result
result = power(num,ToThePower)
print('{0}的{1}次方是:{2}'.format(num,ToThePower,result))