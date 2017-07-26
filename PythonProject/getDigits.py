def get_digtis(n=1):
   # n = int(n)
    if n<10:
        print(n)
    else:
        print('{0},'.format(n%10),end='')
        get_digtis(int(n/10))

get_digtis(n=12345)