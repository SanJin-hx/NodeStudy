# def discounts(price,rate):
#     final_price = price*rate
#     old_price = 50 #新的局部
#     print('修改后全局变量old_price1:',old_price)
#     return final_price
#
# old_price = float(input('原价:')) #全局
# rate = float(input('折扣:'))
# new_price = discounts(old_price,rate)
# print('修改后全局变量old_price2:',old_price)
# print('原价{0}打折后:{1}'.format(old_price,new_price))
#
# if ord(list(each)) in range(65, 91) or ord(list(each)) in range(97, 123):
#     iLetter += 1
# elif each.count(' '):
#     iSpace += 1
# elif ord(list(each)) in range(48, 58):
#     iNumber += 1
# else:
#     iOther += 1

# def FunX(x):
#     def FunY(y):
#         return x*y
#     return FunY
# #i = FunX(8)
# print(FunX(5)(8))

# def Fun1():
#     x = 5
#     def Fun2():
#         nonlocal x
#         x *= x
#         return x
#     return Fun2()
# print(Fun1())
# if i >= 3 and i <= passlength - 3:
#     n = i + 3
#     for j in range(0, i):
#         if ord(passlist[j]) in range(65, 91):
#             prevc += passlist[j]
#     for k in range(i, n):
#         if ord(passlist[k]) in range(65, 91):
#             nextc += passlist[k]

# list1 = list(filter(lambda x : not(x%3),range(101)))
# list2 = list(map(lambda x : x*2,range(10)))
# print(list1)

# def recursion(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
# print(recursion(5))

# def test():
#     dictt = {1: '1'}
#     return dictt
#
# dictt = {1:'1'}
# print(id(dictt)==id(test()))
# print(test())
#
# sentinel = 'end'
#
# lines = []
# print('请输入内容【输入end结束】:',end='')
# for line in iter(input,sentinel):
#     lines.append(line)
#
# print(lines)
# f = open('testfile.txt')
# f1 = open('testfile1.txt')
# fileread = []
# fileread1 = []
# for line in f.readlines()[1:3]:
#     fileread.append(line)
#
# f.close()
# f1.close()
# print(fileread)
# print(fileread1)
# for lines in f:
#     fileread.append(lines)
# f.close()
# for lines in f1:
#     fileread1.append(lines)
# f1.close()
#
# print(fileread)
# print(fileread1)

# str = '13:'
# print(str.split(':'))
# print(str.split(':')[1]=='')

# import sys
# import re
# f = open('%s'%'testfile.txt')
# text = f.read()
# goal ='倒车'
#
# allchars = re.findall(r'%s' % goal,text)
#
# allchar_dict = dict([(all,0) for all in allchars])
#
# for allchar in allchars:
#     allchar_dict[allchar] = allchar_dict[allchar]+1
# print(allchar_dict)
# f.close()
# f = open('testfile.txt','+r')
# text = f.readlines()
# f.seek(0)
# f.truncate()
# for char in text:
#     char = char.replace('倒车','yy')
#     f.write(char)
# f.close()


