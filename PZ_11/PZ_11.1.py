import os


def task1():
    """
    Создаёт файл с числами, обрабатывает их и формирует отчёт.
    """
    try:
        # 1. Формируем исходный файл с числами
        numbers = [12, -5, 8, -3, 20, -15, 7, 9, -1, 4]
        with open('numbers.txt', 'w', encoding='utf-8') as f:
            f.write(' '.join(map(str, numbers)))
        
        # 2. Читаем и обрабатываем числа
        with open('numbers.txt', 'r', encoding='utf-8') as f:
            data = f.read().strip()
            if not data:
                raise ValueError("Файл numbers.txt пуст.")
            num_list = list(map(int, data.split()))
        
        # 3. Вычисляем требуемые показатели
        count = len(num_list)
        reversed_nums = num_list[::-1]
        half = count // 2
        sum_last_half = sum(num_list[half:])
        
        # 4. Записываем отчёт в новый файл
        with open('report.txt', 'w', encoding='utf-8') as f:
            f.write("Исходные данные:\n")
            f.write(' '.join(map(str, num_list)) + '\n')
            f.write(f"Количество элементов: {count}\n")
            f.write("Элементы в обратном порядке:\n")
            f.write(' '.join(map(str, reversed_nums)) + '\n')
            f.write(f"Сумма элементов последней половины: {sum_last_half}\n")
        
        print("Задача 1 выполнена. Файлы 'numbers.txt' и 'report.txt' созданы.")
        
    except Exception as e:
        print(f"Ошибка в задаче 1: {e}")


def task2(input_filename='text18-10.txt', output_filename='poem.txt'):
    """
    Читает файл, подсчитывает заглавные буквы, создаёт стихотворную версию с автором.
    """
    try:
        if not os.path.exists(input_filename):
            sample_text = """Ветер по морю гуляет
И кораблик подгоняет
Он бежит себе в волнах
На раздутых парусах"""
            with open(input_filename, 'w', encoding='utf-8') as f:
                f.write(sample_text)
            print(f"Создан пример файла '{input_filename}'.")
        
        with open(input_filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        print(f"Содержимое файла '{input_filename}':")
        uppercase_count = 0
        for line in lines:
            print(line.rstrip())
            uppercase_count += sum(1 for ch in line if ch.isupper())
        
        print(f"\nКоличество букв в верхнем регистре: {uppercase_count}")
        
        with open(output_filename, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line)
            f.write("\n\nАвтор: Александр Пушкин\n")
            f.write("Название: Сказка о царе Салтане\n")
        
        print(f"Задача 2 выполнена. Файл '{output_filename}' создан.")
        
    except Exception as e:
        print(f"Ошибка в задаче 2: {e}")


if __name__ == '__main__':
    print("Практическое занятие №11. Вариант 10")
    print("=" * 50)
    task1()
    print("-" * 30)
    task2()
    print("=" * 50)
    print("Работа завершена.")