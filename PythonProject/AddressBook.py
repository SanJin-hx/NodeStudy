import sys
def main_interface():
    select = input('请输入相关指令代码:')
    if select == '1':
        Refer()
    elif select == '2':
        New_contact()
    elif select == '3':
        Delet()
    elif select == '4':
        sys.exit(0)

def New_contact():
    global Phone_book
    name = input('请输入联系人姓名:')
    if name in Phone_book.keys():
        print('您输入的用户名在通讯录中已存在-->>{0}:{1}'.format(name, Phone_book[name]))
        choice = input('是否更改用户(Yes/No):')
        if choice == 'Yes' or choice == 'Yes' or choice == 'yes' or choice == 'y':
            change = input('请输入用户联系电话:')
            Phone_book[name] = change
            main_interface()
        else:
            main_interface()
    else:
        choice = input('您输入的用户不存在,是否新建用户(Yes/No):')
        if choice == 'Yes' or choice == 'Yes' or choice == 'yes' or choice == 'y':
            usename = input('请输入联系人姓名:')
            phonenum = input('请输入联系人电话号码')
            Phone_book[usename] = phonenum
            print('用户插入成功')
            main_interface()
        else:
            main_interface()

def Delet():
    global Phone_book
    name = input('请输入联系人姓名:')
    if name in Phone_book.keys():
        print('您输入的用户名在通讯录中已存在-->>{0}:{1}'.format(name,Phone_book[name]))
        choice = input('是否删除用户(Yes/No):')
        if choice == 'Yes' or choice == 'Yes' or choice == 'yes' or choice == 'y':
            Phone_book.pop(name)
            print('用户已删除')
            main_interface()
        else:
            main_interface()
    else:
        print('您输入的用户不存在')
        main_interface()
def Refer():
    global Phone_book
    name = input('请输入联系人姓名:')
    if name in Phone_book.keys():
        print('您输入的用户名在通讯录中已存在-->>{0}:{1}'.format(name, Phone_book[name]))
        main_interface()
    else:
        print('您输入的用户不存在')
        main_interface()

global Phone_book
Phone_book = dict()
print('1.查询联系人资料')
print('2.插入新的联系人')
print('3.删除已有联系人')
print('4.退出程序')
main_interface()