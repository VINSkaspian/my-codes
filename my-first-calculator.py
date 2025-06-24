while True: 

    user_input = input(
    "Press 'stop' or 'Enter', by next step: "
    )

    if user_input == "stop":
        print("Program is finish, baye!")
        break

    try: 
        num = int(input("Enter number plese: "))
        print("Yor number: ",num)
    except ValueError:
        print (
        "ERROR: Enter number(incorrect symbols)!"
        )

    # try:
    # опасный код
    # except Ошибка:
    # что делать, если она случилась

    a = int(input("Enter first number "))
    operation = input(
        "Choose operation ( + - * / ) "
        )
    
    b = int(input("Enter last number "))
    if operation == '+' :
        result = a + b 

    elif operation == '-' :
        result = a - b 

    elif operation == '*' :
        result = a * b

    elif operation == '/':

        if b != 0 :
            resut = a / b

        else:
           resul = "ERROR: division by 0 "

    else:
        result = "UNKNOV OPERATION "

    print ('Результат',result)


