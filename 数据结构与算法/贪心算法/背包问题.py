# 贪心算法求解背包问题，而不适用于0-1背包问题
def fractional_backpack(goods, w):
    """

    :param goods:是一个二阶矩阵，每一行由商品价值+重量
    :param w: 背包最大载重量
    :return:物体选择情况
    """
    # # 创建一个和goods一样长但全是0的列表
    m = [0 for _ in range(len(goods))]
    # 总价值
    total_v = 0
    # 重点，重点，重点：goods是一个二阶矩阵，enumerate枚举函数
    # i 表示每一行的索引；（price，weight）作为一个整体的值
    for i, (price, weight) in enumerate(goods):
        # print(i)
        # print(price)
        # print(weight)
        if w >= weight:
            m[i] = 1
            total_v += price
            w -= weight
        else:
            # 大意为：剩余背包容量最多容纳物体的一部分，用剩余容量乘以价值
            m[i] = w / weight
            total_v += m[i] * price
            w = 0
            break
    return m, total_v


goods = [[60, 10],
         [100, 20],
         [120, 30]]

print(fractional_backpack(goods, 50))
