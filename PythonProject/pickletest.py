#pickle 腌制

import pickle
#dumps(obj)将对象序列化
lista = ['stream','ea','ub']
listb = pickle.dumps(lista)
#print (listb)

#loads(string)将对象原样恢复，并且对象类型也回复为原来格式
listc = pickle.loads(listb)
#print (listc)

#dump(obj,file),将对象存储到文件里序列化
group1 = ('baidu','google','tx')
f1 = open('1.pk1','wb')
pickle.dump(group1,f1,True)
f1.close()

#load(obj,file),将dump()存储在文件里的数据恢复
f2 = open('1.pk1','rb')
t = pickle.load(f2)
print (t)
f2.close()
