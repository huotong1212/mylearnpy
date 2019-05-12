

import os
# 要删除的目录路径
os.chdir("D:\\000\\111")
list3 = os.listdir("D:\\000\\111")


def clear_file(list1, path):
    if len(list1) > 0:
        for f in list1:
            if os.path.isfile(path + "\\%s" % f):
                os.remove(path + "\\%s" % f)
            else:
                os.chdir(path + "\\%s" % f)
                list2 = os.listdir(path + "\\%s" % f)
                # 递归
                clear_file(list2, path + "\\%s" % f)

                os.chdir(path)
                os.rmdir(f)


clear_file(list3, "D:\\000\\111")
