def cuentaRegresiva(n):
    while n > 0:
        print(n)
        n -= 1
    print("Booooom")


# cuentaRegresiva(5)

def factorial(num):
    print("Valor inicial -> ", num)
    if num > 1:
        num = num * factorial(num - 1)
    print("Valor final -> ", num)
    return num


print(factorial(5))
