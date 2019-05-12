
import json

### dumps将python转换为json字符串格式
dic = {'name':'Micheal'}
jstr = json.dumps(dic)
print(jstr,type(jstr))


### dump将python对象转换为json字符串格式，并写入文件
with open('jsonTest.txt','w',encoding='utf-8') as f:
    json.dump(dic,f)
    #f.write(json.dumps(dic))

### loads将json字符串转化为python对象格式
jdic = json.loads(jstr)
print(jdic,type(jdic))

### load从文件中读取json字符串并转换为python对象格式
with open('jsonTest.txt','r',encoding='utf-8') as f:
    data = json.load(f)
    # data = json.loads(f.read())
    print(data,type(data))