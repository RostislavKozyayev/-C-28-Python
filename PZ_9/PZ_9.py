# Организовать словарь avto, содержащий 3 ключа (марки авто) и списки
# из трех моделей в качестве значений. Обеспечить отображение вторых моделей по
# каждому авто, всех моделей словаря.

# Создаем словарь avto с марками и моделями
avto = {
    "Toyota": ["Corolla", "Camry", "RAV4"],
    "Honda": ["Civic", "Accord", "CR-V"],
    "Ford": ["Focus", "Mustang", "Explorer"]
}

# Выводим вторые модели для каждой марки
print("Вторые модели каждой марки:")
for brand, models in avto.items():
    print(f"{brand}: {models[1]}")

# Выводим все модели словаря
print("\\nВсе модели словаря:")
for brand, models in avto.items():
    print(f"{brand}: {', '.join(models)}")