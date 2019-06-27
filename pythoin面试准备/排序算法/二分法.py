class ToFind(object):

    def find(self, arr, num, start, end):

        # 取中位数
        mid = (start + end) // 2

        if num == arr[mid]:
            index = mid
        elif end - start == 1 and arr[start] != num and arr[end] != num:
            index = '你要找的数不在这个数组里面'
        elif num < arr[mid]:
            index = self.find(arr, num, 0, mid)
        elif num > arr[mid]:
            index = self.find(arr, num, mid, end)

        return index


if __name__ == '__main__':
    arr = [2, 3, 5, 10, 15, 16, 18, 22, 26, 30, 32, 35, 41, 42, 43, 55, 56, 66, 67, 69, 72, 76, 82, 83, 88];

    tofind = ToFind()
    print(arr.index(55))
    print(tofind.find(arr, 8, 0, len(arr)))
