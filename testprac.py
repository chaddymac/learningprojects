def add(num1, num2):
    if type(num1) == str or type(num2) == str:
        raise Exception("type error")
    
    return num1 + num2

print(add(6, 5))

