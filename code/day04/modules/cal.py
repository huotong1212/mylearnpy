
import os

os.makedirs('D:\\000\\111\\222\\333',exist_ok=True) #若存在，不创建
os.chdir('D:\\000\\111\\222\\333')
file = open('test','w',encoding='utf-8')
file.close()
os.chdir('D:\\000\\111\\222')
with open('test2','ab') as f:
    f.write('\nDoctor HuaSheng'.encode('utf-8'))

# print(eval('1+1'))