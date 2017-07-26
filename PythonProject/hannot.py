def hannoi(n,x,y,z):
    if n==1:
        print(x,'->',z)
    else:
        hannoi(n-1,x,z,y)
        print(x, '->', z)
        hannoi(n-1,y,x,z)

hannoi(3,'a','b','c')