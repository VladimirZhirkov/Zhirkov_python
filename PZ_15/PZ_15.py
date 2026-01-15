import sqlite3
from datetime import date

def create_database():
    conn = sqlite3.connect('industry.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enterprises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            address TEXT,
            branches INTEGER,
            staff INTEGER,
            equipment_cost REAL,
            production_volume REAL,
            registration_date DATE
        )
    ''')
    conn.commit()
    conn.close()

def insert_sample_data():
    conn = sqlite3.connect('industry.db')
    cursor = conn.cursor()
    sample_data = [
        ('IND001', 'Завод "Машиностроитель"', 'ул. Ленина, 15', 3, 500, 2500000.0, 15000.0, '2020-05-10'),
        ('IND002', 'Фабрика "Текстиль"', 'пр. Мира, 42', 1, 200, 800000.0, 5000.0, '2019-08-22'),
        ('IND003', 'Комбинат "Пищевик"', 'ул. Советская, 7', 5, 800, 3500000.0, 28000.0, '2021-01-15'),
        ('IND004', 'Завод "Химволокно"', 'ул. Промышленная, 33', 2, 350, 1200000.0, 9000.0, '2018-11-30'),
        ('IND005', 'Фабрика "Мебель"', 'ул. Деревообработки, 12', 0, 120, 600000.0, 4000.0, '2022-03-05'),
        ('IND006', 'Завод "Электроника"', 'пр. Космонавтов, 21', 4, 650, 5000000.0, 32000.0, '2020-07-18'),
        ('IND007', 'Комбинат "Стройматериалы"', 'ул. Цементная, 5', 3, 400, 1800000.0, 12000.0, '2019-04-25'),
        ('IND008', 'Фабрика "Одежда"', 'ул. Ткацкая, 9', 1, 180, 750000.0, 6000.0, '2021-09-12'),
        ('IND009', 'Завод "Автодеталь"', 'пр. Автомобилистов, 77', 6, 900, 4200000.0, 35000.0, '2022-02-28'),
        ('IND010', 'Комбинат "Бумага"', 'ул. Лесная, 3', 2, 300, 1500000.0, 11000.0, '2020-12-01')
    ]
    cursor.executemany('''
        INSERT OR IGNORE INTO enterprises 
        (code, name, address, branches, staff, equipment_cost, production_volume, registration_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', sample_data)
    conn.commit()
    print("Добавлено 10 записей в таблицу enterprises.")
    conn.close()

def search_enterprises():
    conn = sqlite3.connect('industry.db')
    cursor = conn.cursor()
    
    print("\n1. Поиск предприятий с численностью персонала > 500:")
    cursor.execute('SELECT code, name, staff FROM enterprises WHERE staff > ?', (500,))
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]} ({row[2]} чел.)")
    
    print("\n2. Поиск предприятий с филиалами >= 3:")
    cursor.execute('SELECT code, name, branches FROM enterprises WHERE branches >= ?', (3,))
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]} ({row[2]} филиалов)")
    
    print("\n3. Поиск предприятий, зарегистрированных после 2020-01-01:")
    cursor.execute('SELECT code, name, registration_date FROM enterprises WHERE registration_date > ?', ('2020-01-01',))
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]} ({row[2]})")
    
    conn.close()

def delete_enterprises():
    conn = sqlite3.connect('industry.db')
    cursor = conn.cursor()
    
    print("\n1. Удаление предприятий без филиалов:")
    cursor.execute('DELETE FROM enterprises WHERE branches = 0')
    print(f"   Удалено записей: {cursor.rowcount}")
    
    print("\n2. Удаление предприятий с объёмом производства < 10000:")
    cursor.execute('DELETE FROM enterprises WHERE production_volume < ?', (10000,))
    print(f"   Удалено записей: {cursor.rowcount}")
    
    print("\n3. Удаление предприятий с кодом 'IND004':")
    cursor.execute('DELETE FROM enterprises WHERE code = ?', ('IND004',))
    print(f"   Удалено записей: {cursor.rowcount}")
    
    conn.commit()
    conn.close()

def update_enterprises():
    conn = sqlite3.connect('industry.db')
    cursor = conn.cursor()
    
    print("\n1. Увеличение стоимости оборудования на 10% для предприятий с staff > 400:")
    cursor.execute('UPDATE enterprises SET equipment_cost = equipment_cost * 1.1 WHERE staff > ?', (400,))
    print(f"   Обновлено записей: {cursor.rowcount}")
    
    print("\n2. Установка количества филиалов = 2 для предприятий с 1 филиалом:")
    cursor.execute('UPDATE enterprises SET branches = 2 WHERE branches = 1')
    print(f"   Обновлено записей: {cursor.rowcount}")
    
    print("\n3. Обновление адреса для предприятия с кодом 'IND006':")
    cursor.execute('UPDATE enterprises SET address = ? WHERE code = ?', ('пр. Космонавтов, 21 (новый корпус)', 'IND006'))
    print(f"   Обновлено записей: {cursor.rowcount}")
    
    conn.commit()
    conn.close()

def display_all():
    conn = sqlite3.connect('industry.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM enterprises')
    rows = cursor.fetchall()
    print("\nТекущее состояние таблицы enterprises:")
    print("ID | Код      | Наименование                   | Персонал | Оборудование   | Продукция")
    for row in rows:
        print(f"{row[0]:2} | {row[1]:8} | {row[2]:30} | {row[5]:8} | {row[6]:13.2f} | {row[7]:10.2f}")
    conn.close()

if __name__ == '__main__':
    print("Практическое занятие №15. Вариант 10: ПРОМЫШЛЕННОСТЬ")
    print("=" * 70)
    
    create_database()
    insert_sample_data()
    display_all()
    
    print("\n" + "="*70)
    print("ВЫПОЛНЕНИЕ ПОИСКА:")
    search_enterprises()
    
    print("\n" + "="*70)
    print("ВЫПОЛНЕНИЕ УДАЛЕНИЯ:")
    delete_enterprises()
    display_all()
    
    print("\n" + "="*70)
    print("ВЫПОЛНЕНИЕ ОБНОВЛЕНИЯ:")
    update_enterprises()
    display_all()
    
    print("\n" + "="*70)
    print("Работа завершена.")