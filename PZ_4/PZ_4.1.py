# Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все
# целые степени числа A от 1 до N.


# Вводим вещественное число A и целое число N
while True:
    try:
        A = float(input("Введите вещественное число A: "))
        print("Удачно")
        break
    except ValueError:
        print("Что-то пошло не так. Повторите попытку.")

while True:
    try:
        N = int(input("Введите целое число N (>0): "))
        if N <= 0:
            print("Ошибка: N должно быть больше 0.")
            continue
        print("Удачно")
        break
    except ValueError:
        print("Что-то пошло не так. Повторите попытку.")

# Выводим целые степени числа A от 1 до N
for i in range(1, N + 1):
    power = A ** i
    print(f"{A}^{i} = {power}")