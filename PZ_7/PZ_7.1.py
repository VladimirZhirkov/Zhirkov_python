def reverse_string():
    try:
        s = input("Введите строку: ")
        if not s:
            raise ValueError("Строка не должна быть пустой.")
        
        reversed_s = s[::-1]
        print("Исходная строка:", s)
        print("Перевёрнутая строка:", reversed_s)
    
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    reverse_string()