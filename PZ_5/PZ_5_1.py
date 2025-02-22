#Дано целое число N (> 1). Найти наибольшее целое число K, при котором
#выполняется неравенство 3K < N.

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
