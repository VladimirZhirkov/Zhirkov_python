import random

def task1():
    print("Задача 1: Замена элементов третьей строки матрицы")
    
    rows, cols = 5, 5
    matrix = [[random.randint(-10, 20) for _ in range(cols)] for _ in range(rows)]
    
    print("Исходная матрица:")
    for row in matrix:
        print(row)
    
    new_row = [random.randint(1, 10) for _ in range(cols)]
    
    matrix[2] = new_row
    
    print("\nМатрица после замены третьей строки:")
    for row in matrix:
        print(row)
    print(f"Новая третья строка: {new_row}")

def task2():
    print("\nЗадача 2: Среднее арифметическое положительных элементов матрицы")
    
    rows, cols = 4, 4
    matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
    
    print("Исходная матрица:")
    for row in matrix:
        print(row)
    
    positive_numbers = [num for row in matrix for num in row if num > 0]
    
    if positive_numbers:
        average = sum(positive_numbers) / len(positive_numbers)
        print(f"\nПоложительные элементы: {positive_numbers}")
        print(f"Среднее арифметическое положительных элементов: {average:.2f}")
    else:
        print("В матрице нет положительных элементов.")

if __name__ == '__main__':
    print("Практическое занятие №13. Вариант 10")
    print("=" * 50)
    task1()
    task2()
    print("=" * 50)
    print("Работа завершена.")