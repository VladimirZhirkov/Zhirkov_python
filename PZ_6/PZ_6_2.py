def count_monotonic_segments():
    """Считает количество монотонных участков в списке."""
    try:
        n = int(input("Введите размер списка N: "))
        a = []
        for i in range(n):
            a.append(int(input(f"Введите элемент {i + 1}: ")))
        
        count = 0
        direction = None  
        
        for i in range(1, n):
            if a[i] > a[i - 1]:
                new_dir = 1
            elif a[i] < a[i - 1]:
                new_dir = -1
            else:
                new_dir = 0
            
            if new_dir != 0:
                if direction != new_dir:
                    count += 1
                    direction = new_dir
            else:
                direction = None
        
        print("Количество монотонных участков:", max(0, count))
    
    except ValueError:
        print("Ошибка: введите целые числа.")
        count_monotonic_segments()

count_monotonic_segments()