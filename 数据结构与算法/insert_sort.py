def insert_sort(alist):
    n =len(alist)
    for j in range(1,n):
        i=j
        """
        i代表内层循环起始值
        执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        """
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i -=1
            else:
                break
def main():
    li = [8, 96, 1, 2, 5, 61, 7, 33, 110]
    print(li)
    insert_sort(li)
    print(li)

if __name__ == '__main__':
    main()
