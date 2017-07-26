file_name = input('请输入要打开的文件(c//read.txt):')
file_line = input('请输入要显示的行数【格式如 13:12 或 :12 或 12:】:')

def readConetnt(file_name,file_line):
    file_open = open(file_name)
    file_line = file_line.split(':')
    if len(file_line)>0:
        if file_line[0] != '' and file_line[1]!='':
            print('文件'+file_name+'从第%d行到第%d行内容如下:' % (int(file_line[0]),int(file_line[1])))
            for line in file_open.readlines()[int(file_line[0]):int(file_line[1])]:
                print(line,end='')
                file_open.close()
        elif file_line[0] != '' and file_line[1] == '':
            print('文件' + file_name + '从第%d行开始后内容如下:' % int(file_line[0]))
            for line in file_open.readlines()[int(file_line[0]):]:
                print(line,end='')
                file_open.close()
        elif file_line[0] == '' and file_line[1] != '':
            print('文件' + file_name + '从第%d行开始前内容如下:' % int(file_line[1]))
            for line in file_open.readlines()[:int(file_line[1])]:
                print(line,end='')
                file_open.close()
        else:
            print('文件' + file_name + '内容如下:' )
            for line in file_open.readlines()[:]:
                print(line,end='')
                file_open.close()
    else:
        print('格式错误')
        return

readConetnt(file_name,file_line)

#啊 脑壳疼_(:з」∠)_