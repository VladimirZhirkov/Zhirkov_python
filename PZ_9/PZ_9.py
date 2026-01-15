def manage_fruit_dict():
    
    original_dict = {
        'овощ': 'морковь',
        'напиток': 'сок',
        'десерт': 'торт',
        'ягода': 'клубника'
    }
    
    print("Исходный словарь:")
    for key, value in original_dict.items():
        print(f"  {key}: {value}")
    
    if 'фрукт' in original_dict and original_dict['фрукт'] == 'яблоко':
        print("\nЭлемент 'фрукт: яблоко' уже присутствует в словаре.")
    else:
        original_dict['фрукт'] = 'яблоко'
        print("\nЭлемент 'фрукт: яблоко' добавлен в словарь.")
    
    print("\nИзменённый словарь:")
    for key, value in original_dict.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    manage_fruit_dict()