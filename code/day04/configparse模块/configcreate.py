# configparser模块
# 配置文件解析
import configparser


# 1.创建配置文件
config = configparser.ConfigParser()  # 相当于一个空字典
config['DEFAULT'] = {
            'men':'1',
            'disk':'2',
            'nic':'3'
        }

# 配置文件中新起一块
config['STATICFILES_DIRS'] = {}
# 添加
config['STATICFILES_DIRS']['root'] = 'static'

# 配置文件再起一块
config['TEMPLATEFILES'] = {}

temp_obj = config['TEMPLATEFILES']
temp_obj['root'] = 'templates'

# 写入文件
with open('test.ini', 'w') as configfile:
    config.write(configfile)

# 输出的配置文件内容
# [DEFAULT]
# men = 1
# disk = 2
# nic = 3
#
# [STATICFILES_DIRS]
# root = static
#
# [TEMPLATEFILES]
# root = templates