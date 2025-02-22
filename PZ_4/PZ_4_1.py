#1. Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2N)2

def calculate_sum_of_squares(N):
    try:
        if N <= 0:
            raise ValueError("N должно быть больше 0.")
        
        total_sum = 0
        for i in range(N, 2 * N + 1):
            total_sum += i ** 2 
        
        return total_sum

    except Exception as e:
        return f"Произошла ошибка: {e}"

N = int(input("Введите целое число N (> 0): "))
result_sum = calculate_sum_of_squares(N)
print("Сумма квадратов от", N, "до", 2 * N, "равна:", result_sum)
