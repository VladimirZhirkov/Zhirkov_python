def extract_last_directory():
    try:
        path = input("Введите полный путь к файлу: ")
        
        # Убираем возможные пробелы в начале и конце
        path = path.strip()
        
        if not path:
            raise ValueError("Путь не должен быть пустым.")
        
        # Разделяем путь по символу '\'
        parts = path.split('\\')
        
        # Если путь содержит только имя файла без каталогов
        if len(parts) == 1:
            last_dir = '\\'
        else:
            # Ищем последний каталог (предпоследний элемент, если путь заканчивается на файл)
            if '.' in parts[-1]:  # Последняя часть — файл с расширением
                last_dir = parts[-2] if len(parts) > 1 else '\\'
            else:
                last_dir = parts[-1]
        
        print("Исходный путь:", path)
        print("Название последнего каталога:", last_dir)
    
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    extract_last_directory()