# 二分查找必须采用顺序储存结构，且必须按关键字大小有序排列
def binary_search(data_list, target):
    left = 0
    right = len(data_list) - 1
    index = 1
    while left <= right:
        mid = (left + right) // 2
        if data_list[mid] == target:
            return "一共查找了%d次,此数字在列表中的下标为:%d" % (index, mid)
        elif data_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        index += 1
    return "一共找了%d次,找不到这样的值!" % index


def main():
    target1 = int(input('input this number:'))
    ret1 = binary_search(([1, 3, 6, 8, 9, 13, 61]), target1)
    print(ret1)
    target2 = int(input('chose another number:'))
    ret2 = binary_search(([1, 3, 6, 8, 9, 13, 61]), target2)

    print(ret2)


if __name__ == '__main__':
    main()
