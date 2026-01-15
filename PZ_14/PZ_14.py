import re

def find_dostoevsky_variants(input_file='Dostoevsky.txt', output_file='dostoevsky_variants.txt'):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        pattern = r'\bДостоевск(?:ий|ого|ому|им|ом)\b'
        
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        
        print(f"Найдено вариантов фамилии 'Достоевский' (ед.ч.): {len(matches)}")
        print("Варианты:")
        for match in matches:
            print(f"  - {match}")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Варианты фамилии Достоевский в единственном числе:\n")
            f.write(f"Всего найдено: {len(matches)}\n")
            f.write("Список:\n")
            for match in matches:
                f.write(f"{match}\n")
        
        print(f"\nРезультаты сохранены в файл: {output_file}")
        
    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    print("Практическое занятие №14. Вариант 10")
    print("=" * 60)
    find_dostoevsky_variants()
    print("=" * 60)
    print("Работа завершена.")