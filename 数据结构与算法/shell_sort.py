def shellSort(alist):
    length = len(alist)
    if len(alist) <= 1:
        return alist
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap, length):
            j = i - gap
            temp = alist[i]
            while j >= 0 and temp < alist[j]:
                alist[j + gap] = alist[j]
                j -= gap
            alist[j + gap] = temp
        gap //= 2
    return alist


if __name__ == '__main__':
    alist = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print('\033希尔排序结果：\033')
    print(shellSort(alist))
