A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

is_A_odd = A % 2 != 0
is_B_odd = B % 2 != 0

if is_A_odd ^ is_B_odd:
    print("Ровно одно из чисел A и B нечетное.")
else:
    print("Либо оба числа четные, либо оба нечётные.")
