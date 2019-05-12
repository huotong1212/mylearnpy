
# file = open('test','w',encoding='utf-8')
#
# file.write('111\n')
# file.write('aaa\n')
#
# file.close()
#
# with open('test','a',encoding='utf-8') as f:
#     f.write('dad')
#     f.write('mom')
#     f.write('child')

# with open('fileoperation.py','r',encoding='utf-8') as fo:
#     data = fo.read()
#     print(data)

# fb = open('fileoperation.py','rb')
# data = fb.read()
# print(data.decode('utf-8'))

fb = open('test','ab')
fb.write('\nMR.SherLock'.encode('utf-8'))
fb.write(bytes('\nMRS.DOCTOR',encoding='utf-8'))
fb.close()