file_object = open('string1.txt')
try:
     all_the_text = file_object.read( )
     textlist = list(all_the_text)
finally:
     file_object.close()

def Readfile(text):
    textlength = len(text)
    textstr = ''
    charsnum = 0
    for i in range(0, textlength):
        if ord(text[i]) in range(65, 91) or ord(text[i]) in range(97, 123):
            textstr += text[i]
        else:
            charsnum += 1
    return (textstr,charsnum)
result = Readfile(textlist)
print('In a word:{0},NumberOfChar:{1}'.format(result[0],result[1]))