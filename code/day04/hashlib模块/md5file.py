
#!/usr/bin/env python
#coding: utf-8

import hashlib
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: %s file' % sys.argv[0])

    filename = sys.argv[1]
    m = hashlib.md5()
    with open(filename, 'rb') as fp:
        while True:
            blk = fp.read(4096) # 每次读取4kb
            if not blk: break
            m.update(blk)
    print (m.hexdigest(), filename)

if __name__ == '__main__':
    main()