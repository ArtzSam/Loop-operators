def kratnoe_semi(n):
    # начало - конец - шаг
    for i in range(7, n+1, 7):
        print(i)

n = int(input("Введите целое число n: "))

if n < 7:
    print("Нет чисел, кратных семи ", n)
else:
    print("Числа, кратные семи до", n, ":")
    kratnoe_semi(n)

