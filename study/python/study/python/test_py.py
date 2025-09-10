# 辗转相减法,求最大公约数。
def greatest_common_divisor():
    a = int(input())  # 默认换行为输入结束。
    b = int(input())

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    print("最大公约数为：", a)


greatest_common_divisor()
