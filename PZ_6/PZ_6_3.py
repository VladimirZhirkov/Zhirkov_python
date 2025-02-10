def shift_right():
    """Сдвигает элементы списка вправо и заменяет первый элемент на 0."""
    try:
        n = int(input("Введите размер списка N: "))
        a = []
        for i in range(n):
            a.append(int(input(f"Введите элемент {i + 1}: ")))
        
        a = [0] + a[:-1]
        print("Результирующий список:", a)
    
    except ValueError:
        print("Ошибка: введите целые числа.")
        shift_right()

shift_right()