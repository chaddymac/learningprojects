def highest_even(*args):
    even_num = 0

    for arg in args:
        if arg % 2 == 0 and arg > even_num:
            even_num = arg
    return even_num


num1 = 2
num2 = 6
num3 = 9
num4 = 13
num5 = 12
num6 = 0


result = highest_even(num1, num2, num3, num4, num5, num6)
print(result)

