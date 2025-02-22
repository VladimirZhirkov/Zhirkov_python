def print_multiples_elements():
    """Выводит элементы списка с порядковыми номерами, кратными K."""
    try:
        n = int(input("Введите размер списка N: "))
        k = int(input("Введите число K (1 < K < N): "))
        if k <= 1 or k >= n:
            raise ValueError("K должно быть в диапазоне (1 < K < N).")
        
        a = list(range(1, n + 1))
        print("Список A:", a)
        
        result = [a[i]] for i in range(k - 1, n, k)]
        print(f"Элементы с номерами, кратными {k}:", result)
    
    except ValueError as e:
        print(f"Ошибка: {e}")
        print_multiples_elements()

print_multiples_elements()
