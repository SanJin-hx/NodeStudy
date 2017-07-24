'分别统计传入字符串参数的英文字母、空格、数字和其他字符的个数'
strs = input('请输入任意字符串:')

def countchar(*str):
    iLetter = 0
    iSpace = 0
    iNumber = 0
    iOther = 0
    for each in str:
        eachlist = list(each)
        eachlength = len(eachlist)
        for i in range(0,eachlength):
            if ord(eachlist[i]) in range(65,91) or ord(eachlist[i]) in range(97,123):
                iLetter += 1
            elif eachlist[i] == ' ':
                iSpace += 1
            elif ord(eachlist[i]) in range(48,58):
                iNumber += 1
            else:
                iOther += 1
    return (iLetter,iNumber,iSpace,iOther)

result = countchar(strs)
print('英文字母数:',result[0])
print('数字字数:',result[1])
print('空格数:',result[2])
print('其他字符数:',result[3])
