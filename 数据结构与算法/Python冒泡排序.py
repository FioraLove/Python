def bubbleSort(myList):
    # 首先获取list的总长度,为之后的循环比较作准备
    length = len(myList)

    # 一共进行几轮列表比较,一共是(length-1)轮
    for i in range(0, length - 1):
        bool =True
        # 每一轮的比较,注意range的变化,这里需要进行length-1-长的比较,注意-i的意义(可以减少比较已经排好序的元素)
        for j in range(0, length - 1 - i):

            # 交换
            if myList[j] > myList[j + 1]:
                # tmp = myList[j]
                # myList[j] = myList[j + 1]
                # myList[j + 1] = tmp
                myList[j],myList[j+1]=myList[j+1],myList[j]
                bool =False
        if bool:
            break
        # 打印每一轮交换后的列表
        for item in myList:
            print(item,end=' ')
        print('')


print("冒泡排序执行如下: ")
myList = [1, 4, 5, 0, 6]
bubbleSort(myList)

# 查找算法的改进优化
ef bubble_sort(items):
    k = 0
    for i in range(len(items) - 1):
        flag = False
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                flag = True
                k += 1
                print(items)
        if not flag:
            break
    return items, k


# 冒泡排序优化二：搅拌排序，双向排序提高效率，即当一次从左向右的排序结束后，立马从右向左排序
def new_bubble_sort(items):
    for i in range(len(items) - 1):
        flag = False
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                flag = True

        if flag:
            flag = False
            for j in range(len(items) - 2 - i, 0, -1):
                if items[j - 1] > items[j]:
                    items[j], items[j - 1] = items[j - 1], items[j]
                    flag = True

        if not flag:
            break

    return items


if __name__ == '__main__':
    items = [2, 1, 9, 11, 10, 8, 7]
    a = new_bubble_sort(items)
    print(a)
    print('排列过程为：')
    print('结果为：%s ,排列次数为：%s' % bubble_sort(items))
