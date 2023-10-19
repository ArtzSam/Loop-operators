n = int(input("Введите по порядку целые числа без пробелов и иных знаков: "))
def sum(n):
    total_sum = 0

    while n > 0:
        total_sum += n % 10
        n //= 10

    return total_sum

result = sum(n)
print(f"Сумма цифр числа {n} равна {result}")
