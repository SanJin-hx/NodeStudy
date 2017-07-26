firs_file_name = input('请输入第一个文件名:')
other_file_name = input('请输入要比较的文件名:')
global count
count = 0
def comparefile(first_name,other_name):
    f1 = open(first_name)
    f2 = open(other_name)
    firstfile = []
    otherfile = []
    for lines in f1:
        firstfile.append(lines)
    f1.close()
    for lines in f2:
        otherfile.append(lines)
    f2.close()
    #print(firstfile)
    #print(otherfile)
    if len(firstfile) > len(otherfile):
        printdiff(otherfile,firstfile)
    else:
        printdiff(firstfile, otherfile)

def printdiff(firts,other):
    global count
    keys = []
    for key in range(0,len(firts)):
        if firts[key] != other[key]:
            count += 1
            keys.append(key)
        else:
            continue
    print('两个文件共有{0}处不同:'.format(count))
    for index in keys:
        print('第{0}行不一样'.format(index))

comparefile(firs_file_name,other_file_name)


#啊 写程序写的想死 果然 编程要脑子 散了吧_(:з」∠)_
去个WC 冷静一下