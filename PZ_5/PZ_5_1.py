#1. Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
#результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
#получится нуль?

def sum_of_digits(n):
    """Возвращает сумму цифр числа."""
    return sum(int(digit) for digit in str(abs(n)))

def subtract_until_zero():
    """Вычисляет количество вычитаний суммы цифр до получения нуля."""
    try:
        num = int(input("Введите целое число: "))
        if num <= 0:
            raise ValueError("Число должно быть положительным.")
        
        count = 0
        while num > 0:
            num -= sum_of_digits(num)
            count += 1
        return count
    except ValueError as e:
        print(f"Ошибка: {e}")
        return subtract_until_zero()

result = subtract_until_zero()
print(f"Количество действий: {result}")
