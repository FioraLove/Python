# 法一：
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
    ret1 = binary_search(([3, 6, 8, 9, 13, 61]), target1)
    print(ret1)
    target2 = int(input('chose another number:'))
    ret2 = binary_search(([1, 3, 6, 8, 9, 13, 61]), target2)

    print(ret2)

# 法一（另一种描述）
def find(l, aim, start=0, end=None):
    end = len(l) if end is None else end
    # 计算中间值
    mid_index = (start + end) // 2 + start
    if l[mid_index] < aim:
        find(l, aim, start=mid_index + 1, end=end)

    elif l[mid_index] > aim:
        find(l, aim, start=start, end=mid_index - 1)
    else:
        # 返回数据位置索引
        return mid_index


if __name__ == '__main__':
    main()
    l = [1, 2, 3, 6, 8, 9, 10, 13, 61]
    index = find(l, 8)
    print(index)
    print('------------')
    # 法三：采用for循环遍历
    for i in range(len(l)):
        if l[i] == 7:
            print('该元素位置：', i)

    print('----------')
    # 法四：列表的list.index(obj)方法， 从列表中找出某个值第一个匹配项的索引位置
    print('该元素位置：', l.index(8))
