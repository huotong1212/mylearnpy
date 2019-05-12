import re

'''
（1）.：默认匹配除\n之外的任意一个字符。若指定flag DOTALL,则匹配任意字符，包括换行'''
res = re.match('......', 'li123kunhong123')
print(res.group())  # 结果——li123k

'''
（2）+：匹配前一个字符1次或多次。'''
res = re.match('.+', 'li123kunhong123')
print(res.group())  # 结果——li123kunhong123

'''
（3）^：从开头匹配字符。'''
res = re.match('^li\d+', 'li123kunhong123')
print(res.group())  # 结果——li123

''''
（4）$：匹配字符结尾,
$前面的必须是字符串结尾'''
res = re.search('k.+3$', 'li123kunhong123')  # 获取k开始，中间任意，3结尾的字符串
print(res.group())  # 结果——kunhong123

'''
（5）[]：限制'''
# 匹配中间的英文
res = re.search('k[a-z]+g', 'likunhong123')
print(res.group())  # 结果——kunhong
# 连数字一起匹配
res = re.search('k[a-z0-9]+g', 'likun123hong123')
print(res.group())  # 结果——kun123hong

# 匹配两个井号之间的
res = re.search('#.+#', 'asdf#saffff123#sadf')
print(res.group())  # 结果——#saffff123#

'''
（6）?：匹配?的前一个字符出现或者不出现'''
res = re.search('ax?', 'abcd')  # 意思为ax中的a必须出现，x可以出现或者不出现
print(res.group())  # 结果——a
res = re.search('ax?', 'axbcd')  # 匹配ax，其中a必须出现，x可不出现
print(res.group())  # 结果——ax
res = re.search('a?nnc?', 'asdnnc')  # 匹配annc，其中nn必须出现
print(res.group())  # 结果——nnc

'''
（7）{m}{n,m}：匹配前一个字符m次,匹配前一个字符n到m次'''
res = re.search('[0-9]{3}', 'a1a11a111')
print(res.group())  # 结果——111
res = re.findall('[0-9]{3}', 'a123a113a1114')
print(res)  # 结果——['123', '113', '111']

'''
（8）|：或'''
res = re.search('abc|ABC', 'aaabcAAABC')
print(res.group())  # 结果为abc
res = re.findall('abc|ABC', 'aaabcAAABC')
print(res)  # 结果为['abc', 'ABC']

'''
（9）()：分组匹配'''
res = re.search('abc{2}', '3asfabccasdf')
print(res.group())  # 结果为abcc

res = re.search('(abc){2}(\|\|=)', '857kjhabcabc||=32342')
print(res.group())  # 结果为abcabc||=

'''
'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
'\s'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
'''

'''搞一个大事情'''
a = 'likunhong23student'
b = re.search("(?P<name>[a-zA-Z]+)(?P<age>[0-9]+)(?P<job>\w+)", a).groupdict()
print(b)
# 结果为：{'name': 'likunhong', 'age': '23', 'job': 'student'}

# 可以用来识别身份证号
id = '300100199905120516'
b = re.search('(?P<province>\d{3})(?P<shi>\d{3})(?P<birth>\d{8})(?P<num>\d{2})(?P<last>\d{2})', id).groupdict()
print(b)
# 结果为：{'province': '300', 'shi': '100', 'birth': '19990512', 'num': '05', 'last': '16'}

'''
split()分割'''
res = re.split('[0-9]+', 'ab23bas23basd9989ad')
print(res)  # 结果为['ab', 'bas', 'basd', 'ad']

'''
sub()替换,count不写默认为全体换'''
res = re.sub('[0-9]+', '?', 'abc2abc8abc4d', count=2)
print(res)  # 结果为abc?abc?abc4d

'''
匹配反斜杠'''
res = re.search(r'\\d', 'asdf\dx')
print(res.group())  # 结果为\d

'''
最后是flags'''
# 1、忽略大小写
res = re.search('[a-z]+', 'asdf\dx', flags=re.I)
print(res.group())  # 结果为asdf
# 2、多行模式
res = re.search('^g', '\ngqwqw\ndxas\nadf\nasdf', flags=re.M)
print(res.group())  # 结果为g
# 3、匹配任意字符
res = re.search('.', '\ngqwqw\ndxas\nadf\nasdf', flags=re.S)
print(res.group())  # 结果为g
