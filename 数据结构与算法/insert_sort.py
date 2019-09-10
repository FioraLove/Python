# -*- coding:utf-8 -*-
def insert_sort(data):
    n = len(data)
    for j in range(1, n):
        i = j
        while i > 0:
            if data[i] < data[i - 1]:
                data[i - 1], data[i] = data[i], data[i - 1]
                i -= 1
                print(data)
            else:
                break
    return data


def insertion_sort2(arr):
    """
    二分法插入排序原理：
    外层循环控制循环次数，第二层确定待插入的位置与范围，最后一层循环向后挪动元素的位置，插入待插入的元素。
    count 和 print(arr)为了便于观察过程，可省略。
    """
    for i in range(1, len(arr)):
        tem = arr[i]
        left = 0
        right = i - 1
        count = 0

        # 待插入的值与已排序区域的中间值比较，不断缩小区域范围，直到left和right相遇。
        while left <= right:
            count += 1
            mid = (left + right) // 2
            if arr[i] < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # 当left和right相遇的时候，待插入的位置其实就是left的位置，此时要将left到有序序列的最后一个元素都向后移动一个位置，才能插入元素。
        # 这里一定要用left-1,否则当left的位置就是有序序列的最后一个位置时，j取不到值，后面的元素会被这个位置的元素值覆盖。
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]

        # 插入元素
        if left != i:
            arr[left] = tem
            print(arr)
    print('共循环%s次' % count)
    return arr


def main():
    li = [2, 5, 1, 12, 4, 6, 22, 9]
    arr = [2, 4, 3, 6, 0, 12, 8]
    print('直接插入排序算法的排序过程:')
    print('直接插入排序结果为：', insert_sort(li))
    print('优化后的插入排序算法：')
    insertion_sort2(arr)


if __name__ == '__main__':
    main()
