name = input('请输入待查找的用户名:')
score = [['ea','50'],['ub','80'],['steam','80'],['bzz','80'],['sony','80']]
IsFind = False
for each in score:
    if name == each[0]:
        print(name+'的得分是:',each[1])
        IsFind = True
        break

if IsFind == False:
    print('数据不存在')