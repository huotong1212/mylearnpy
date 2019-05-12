
import os

# os.makedirs('D:\\000\\111\\222\\333',exist_ok=True) #若存在，不创建
# os.chdir('D:\\000\\111\\222\\333')
# file = open('test','w',encoding='utf-8')
# file.close()
# os.chdir('D:\\000\\111\\222')
# with open('test2','ab') as f:
#     f.write('\nDoctor HuaSheng'.encode('utf-8'))

path = 'D:\\000\\111'
list1 = os.listdir(path)

def clear_mir(list1,path):
    #global path  # 引用全局变量，不写会报错local variable 'path' referenced before assignment
                 # 对象还未声明就被引用
    print('---------------')
    print(list1)
    if len(list1)>0: # 如果文件夹不为空
        for file in list1: # 遍历文件夹中的文件
            path = os.path.join(path,file)

            if os.path.isfile(file): #如果是文件
                os.remove(file)  #删除文件
                # path = os.path.dirname(path) #获取上层目录路径
                print('path:' + path)
            else: #如果是文件夹
                os.chdir(path) # 进入该文件夹
                list2 = os.listdir(path)
                clear_mir(list2,path)

                path = os.path.dirname(path) #获取上层目录路径
                os.chdir(path) #进入上层目录,同时将path改为上层目录
                os.rmdir(file) #删除该文件夹
                print('path:' + path)

# clear_mir(list1,path)
# os.chdir('D:\\000\\111')
# print(os.getcwd())
# print(os.path.isfile('test2'))

def clear_totally(path):
    list1 = os.listdir(path)
    clear_mir(list1,path)
    print('------',len(os.listdir(path)))
    if len(os.listdir(path)) == 0 :
        os.chdir(os.path.dirname(path))
        os.rmdir(path)

clear_totally(path)