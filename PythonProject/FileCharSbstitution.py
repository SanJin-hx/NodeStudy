import re
file_name = input('请输入文件名:')
replace_char = input('请输入要替换的单词或字符串:')
new_char = input('请输入新的单词或字符串:')

def replaceChar(file_name,replace_char,new_char):
    f = open('%s'%file_name)
    f1 = open(file_name,'+r')
    text = f.read()
    goal = replace_char
    allchars = re.findall(r'%s' % goal,text)
    allchar_dict = dict([(all,0) for all in allchars])

    for allchar in allchars:
        allchar_dict[allchar] = allchar_dict[allchar]+1

    if allchar_dict[allchar]!=None:
        print('文件' + file_name +'共有%d个【%s】您确定要把所有的【%s】替换成【%s】吗?' % (allchar_dict[allchar],replace_char,replace_char,new_char))
        choice = input('YES/NO:')
        choice_list = ['YES','y','yes']
    else:
        print('文件无内容')
        f.close()
        f1.close()

    if choice in choice_list:
         texts = f1.readlines()
         f1.seek(0)
         f1.truncate()
         for char in texts:
             char = char.replace(replace_char,new_char)
             f1.write(char)
         f1.close()
    else:
        f1.close()
        f.close()

replaceChar(file_name,replace_char,new_char)

