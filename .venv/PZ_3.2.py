# Даны три целых числа. Найти количество положительных и количество
# отрицательных чисел в исходном наборе.

# Вводим три целых числа
numbers = []
count = 0

while count < 3:
    try:
        number = int(input(f"Введите {count + 1}-е целое число: "))
        print("Удачно")
    except ValueError:
        print("Что-то пошло не так")
        print("Прекращение работы программы")
    numbers.append(number)
    count += 1

# Инициализация счетчиков
positive_count = 0
negative_count = 0

# Подсчитываем положительные и отрицательные числа
i = 0
while i < len(numbers):       # len считает кол-во элементов в списке
    if numbers[i] > 0:
        positive_count += 1
    elif numbers[i] < 0:
        negative_count += 1
    i += 1

# Выводим результаты
print(f"Количество положительных чисел: {positive_count}")
print(f"Количество отрицательных чисел: {negative_count}")