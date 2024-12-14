month = int(input("Введите номер месяца (от 1 до 12): "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
elif month == 2:
    days = 28
else:
    days = "Неверный номер месяца."

print("Количество дней в месяце:", days)