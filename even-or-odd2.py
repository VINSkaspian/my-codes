while True:
    user_input = input("Введите число (или 'stop' для выхода): ")

    if user_input == "stop":
        print("Программа завершена.")
        break

    number = int(user_input)

    if number % 2 == 0:
        print("Чётное число")
    else:
        print("Нечётное число")

