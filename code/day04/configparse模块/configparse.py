# 2.配置文件的增删改查
import configparser


config = configparser.ConfigParser()
# 读取文件
config.read('test.ini')
print(config.sections())
# [DEFAULT]含有特殊意义
# >> ['STATICFILES_DIRS', 'TEMPLATEFILES']

# 取值
print(config['TEMPLATEFILES']['root'])
# >> templates

# 判断存在
print('TEMPLATEFILES' in config)
# >> True

# 遍历值
for key in config['TEMPLATEFILES']:
    print(key)
# >> root men disk nic # 将DEFAULT中的键也遍历出来了,因为[DEFAULT]含有特殊意义;
# 那么[DEFAULT]有什么用？存放通用，都需要的配置；

# 取键
print(config.options('TEMPLATEFILES'))
# >> ['root', 'men', 'disk', 'nic']

# 取键值对
print(config.items('TEMPLATEFILES'))
# >> [('men', '1'), ('disk', '2'), ('nic', '3'), ('root', 'templates')]

# 取对应块下键的值
print(config.get('TEMPLATEFILES', 'root'))
# >> print(config.get('TEMPLATEFILES', 'root')) 同样可以获取[DEFAULT]中键的值

# 删，改，增
# config.write(open('test.ini','w'))
# 1.增
# 添加块
config.add_section('IMAGES')
# 给块添加键值
config.set('IMAGES', 'root', '1.png')
# 保存/写入
config.write(open('test.ini','w'))
# 2.删
# 删除块
config.remove_section('IMAGES')
# 删除对应块下的键值对
config.remove_option('IMAGES', 'root')