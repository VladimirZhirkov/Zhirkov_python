def find_max_K(N):
    try:
        if N <= 1:
            raise ValueError("N должно быть больше 1.")
        
        K = 0
        
        while 3 * (K + 1) < N:
            K += 1
        
        return K

    except Exception as e:
        return f"Произошла ошибка: {e}"

N = int(input("Введите целое число N (> 1): "))
result_K = find_max_K(N)
print("Наибольшее целое число K, при котором 3K < N:", result_K)