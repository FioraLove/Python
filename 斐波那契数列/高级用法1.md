# 递归
def fibonacci(i):
    num_list = [0, 1]
    if i < 2:
        return num_list[i]
    elif i >= 2:
        return (fibonacci(i - 2) + fibonacci(i - 1))


print(fibonacci(10))

----------------------------------------------------
# 矩阵推论
def fib(n):
    if n < 1:
        return (1, 0)

    f_m_1, f_m = fib(n >> 1)
    if n & 1:
        return f_m_1 * (f_m_1 + 2 * f_m), f_m ** 2 + f_m_1 ** 2
    else:
        return f_m_1 ** 2 + f_m ** 2, f_m * (2 * f_m_1 - f_m)
