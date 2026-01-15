import string
import random

def task1():
    n = 12
    numbers = [random.randint(-20, 20) for _ in range(n)]
    
    print("Исходная последовательность чисел:")
    print(numbers)
    
    negative_numbers = [x for x in numbers if x < 0]
    max_negative = max(negative_numbers) if negative_numbers else None
    
    multiples_of_two = [x for x in numbers if x % 2 == 0]
    
    sum_multiples = sum(multiples_of_two)
    
    print(f"\n1. Максимальный среди отрицательных: {max_negative}")
    print(f"2. Элементы, кратные двум: {multiples_of_two}")
    print(f"3. Их сумма: {sum_multiples}")

def task2():
    text = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high."
    
    print("\nИсходная строка:")
    print(text)
    
    digits = [char for char in text if char in string.digits]
    
    print(f"\nЦифры в строке: {digits}")
    print(f"Количество цифр: {len(digits)}")
    print(f"Строка из цифр: {''.join(digits)}")

if __name__ == '__main__':
    print("Практическое занятие №12. Вариант 10")
    print("=" * 50)
    task1()
    task2()
    print("=" * 50)
    print("Работа завершена.")