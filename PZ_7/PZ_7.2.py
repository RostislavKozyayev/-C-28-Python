# Дана строка-предложение на русском языке. Подсчитать количество содержащихся в строке гласных букв.

# Создание функции, которая будет считывать и суммировать гласные буквы из строки:
def count_vowels_russian(s):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    count = sum(1 for char in s if char in vowels)
    return count


russian_sentence = "Привет, Мир!"
vowels_count = count_vowels_russian(russian_sentence)
print(f"Количество гласных букв: {vowels_count}")