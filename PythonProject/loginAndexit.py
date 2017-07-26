import sys
global user
user = dict()
print('--新建用户:N/n--')
print('--登录账户:E/e--')
print('--推出程序:Q/q--')
def Order():
    command = input('--请输入指令代码:')
    if command == 'N' or command == 'n':
        register()
    elif command == 'E' or command == 'e':
        login()
    else:
        sys.exit(0)
def register():
    global user
    usename = input('请输入用户名:')
    if usename not in user.keys():
        password = input('请输入密码:')
        user[usename] = password
        print('注册成功')
        Order()
    else:
        usename = input('您输入的用户已存在,请重新输入用户名:')
        password = input('请输入密码:')
        user[usename] = password
        print('注册成功')
        Order()

def login():
    global user
    usename = input('请输入用户名:')
    if usename in user.keys():
        password = input('请输入密码:')
        if password in user.values():
            print('登陆成功')
            Order()
        else:
            print('密码错误')
            Order()
    else:
        usename = input('您输入的用户不存在，请重新输入:')
        if usename in user.keys():
            password = input('请输入密码:')
            if password in user.values():
                print('登陆成功')
                Order()
            else:
                print('密码错误')
                Order()
Order()