def creat_file(file_name,file_details):
    f = open(file_name,'w')
    for lines in file_details:
        f.writelines(lines+'\n')
    f.close()
file_name = input('请输入文件名:')
sentinel = ':w'

lines = []
print('请输入内容【输入:w结束】:',end='')
for line in iter(input,sentinel):
    lines.append(line)
creat_file(file_name,lines)