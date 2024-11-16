# С помощью функций получить вертикальную и горизонтальную линии. Линия
# проводится многократной печатью символа. Заключить слово в рамку из
# полученных линий.


# Создадим функции для получения горизонтальной и вертикальной линий
def draw_horizontal_line(length, symbol='-'):
    return symbol * length


def draw_vertical_line(height, symbol='|'):
    return symbol * height


def print_framed_text(text):
    # Определим длину рамки
    horizontal_line = draw_horizontal_line(len(text) + 4)   # +4 для учёта пробелов и символов углов
    vertical_line = draw_vertical_line(1)   # высота рамки 1

    # Напечатаем рамку
    print(horizontal_line)
    print(vertical_line + ' ' + text + ' ' + vertical_line)
    print(horizontal_line)


print_framed_text(input('Введите слово: '))