
def deal():
    try:
        print('try...')
        r = 10 / int('2')
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')

def handler():
    r = 10 / int('2')
    if r == 10:
        raise ValueError()
    print('result:', r)

def solve():
    r = 10 / int('2')
    assert r != 0, 'r不可能为0'
    print('result:', r)

deal()