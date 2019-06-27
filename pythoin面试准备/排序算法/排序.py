import random


def generateArr():
    return [random.randrange(10) for i in range(7)]


def bubbles(arr):
    # length 为5时，需要排序4次
    for i in range(len(arr) - 1):
        # i=0时，需要比较四次，i=1时，需要比较三次
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertSort(arr):
    # length为5时，需要排序4次
    for i in range(len(arr) - 1):
        # i为0时，j从1开始排序，排序一次
        # i为1时，j从2开始排序，排序两次
        j = i + 1
        while j > 0:
            # 将最小的移动到最前面
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


if __name__ == '__main__':
    arr = generateArr()
    print(arr)
    print(bubbles(arr.copy()))
    print(insertSort(arr.copy()))
