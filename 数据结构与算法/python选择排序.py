# list 传递的参数，order排序 默认为1，升序，否则降序，仅支持整数类型
def selectsort(list, order=1):
    if not isinstance(order, int):
        raise TypeError('order类型错误')
    for i in range(len(list) - 1):
        # 记录最小位置
        min_index = i
        # 筛选出最小数据
        for j in range(i + 1, len(list)):
            if order == 1:
                if list[j] < list[min_index]:
                    min_index = j
            else:
                if list[j] > list[min_index]:
                    min_index = j
            # 交换位置
            if min_index != i:
                list[i], list[min_index] = list[min_index], list[i]
    print(list)

if __name__ == '__main__':
    alist=[3,5,7,1,8,6]
    list = selectsort(alist)
