# Даны три целых числа. Найти количество положительных и количество
# отрицательных чисел в исходном наборе.

# Инициализация переменных для хранения чисел
number1 = None
number2 = None
number3 = None

# Вводим три целых числа
for count in range(3):
    while True:
        try:
            number = int(input(f"Введите {count + 1}-е целое число: "))
            if count == 0:
                number1 = number
            elif count == 1:
                number2 = number
            elif count == 2:
                number3 = number
            print("Удачно")
            break  # Прерываем цикл, если ввод успешен
        except ValueError:
            print("Что-то пошло не так. Пожалуйста, введите целое число.")

# Подсчитываем положительные и отрицательные числа
positive_count = sum(1 for num in [number1, number2, number3] if num > 0)
negative_count = sum(1 for num in [number1, number2, number3] if num < 0)

print(f'Количество положительных чисел: {positive_count}')
print(f'Количество отрицательных чисел: {negative_count}')