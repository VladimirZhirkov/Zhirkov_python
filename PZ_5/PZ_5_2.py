#Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из
#значений X и Y, а в переменную Y — максимальное из этих значений (X и Y —
#вещественные параметры, являющиеся одновременно входными и выходными).
#Используя четыре вызова этой функции, найти минимальное и максимальное из
#данных чисел A, B, C, D.

def minmax(x, y):
    """Обновляет x (минимальное) и y (максимальное) из x и y."""
    if x > y:
        x, y = y, x
    return x, y

def input_numbers():
    numbers = []
    for i in range(4):
        while True:
            try:
                num = float(input(f"Введите число {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Ошибка: введите число.")
    return numbers

a, b, c, d = input_numbers()

a, b = minmax(a, b)
c, d = minmax(c, d)
a, c = minmax(a, c)
b, d = minmax(b, d)

print(f"Минимальное: {a}, Максимальное: {d}")
