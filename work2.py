n = int(input("Введите натуральное число n: "))

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        print(f"{i} * ", end='')  # Выводим перемножаемое число - для наглядности - опционально для задания.
    return result

if n < 0:
    print("Факториал определяется ллишь для неотрицательных чисел")
else:
    result = factorial(n)
    print(f"\n Факториал числа {n} равен {result}")
