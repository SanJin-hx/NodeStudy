def DectoBin(n):
    if n == 0:
        return 0
    else:
        print(n%2,end='')
        DectoBin(int(n/2))

DectoBin(10)