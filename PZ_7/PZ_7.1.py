# Дана строка. Подсчитать количество содержащихся в ней прописных латинских букв.

# Создание функции, которая будет считывать и суммировать буквы, если буква в строке прописная и латинская:
def count_uppercase_letters(s):
    count = sum(1 for char in s if char.isupper() and 'A' <= char <= 'Z')
    return count


string = "Hello, World!"
uppercase_count = count_uppercase_letters(string)
print(f"Количество прописных латинских букв: {uppercase_count}")