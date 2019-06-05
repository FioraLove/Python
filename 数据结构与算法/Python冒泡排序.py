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
