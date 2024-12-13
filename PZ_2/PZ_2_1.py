def main():
    try:
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))

        if A <= 0 or B <= 0:
            raise ValueError("Числа A и B должны быть положительными.")
        if A <= B:
            raise ValueError("A должно быть больше B.")

        незанятая_часть = A % B
        print("Длина незанятой части отрезка A:", незанятая_часть)

    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
