operations = ['Addition', 'Substraction', 'Multipication', 'Division', 'Modular Division', 'Exit']

while True:
    print("Choose Operation : ")

    for index, operation in enumerate(operations, start=1):
        print(f'( {index} ) {operation} ')

    try:
        operator = int(input("Enter Number of Operation:"))
        if operator == 6:
            print("Tata Tata !")
            break

        first_number = int(input("Enter First No : "))
        second_number = int(input("Enter Second No : "))

    except ValueError:
        print("X-X-X  Enter Integer Values Only  X-X-X")
        continue

    if operator == 1:
        result = first_number + second_number

    elif operator == 2:
        result = first_number - second_number

    elif operator == 3:
        result = first_number * second_number

    elif operator == 4:
        result = first_number / second_number

    elif operator == 5:
        result = first_number % second_number

    else:
        print("X-X-X  Invalid Operation Number  X-X-X")
        continue

    print(f'{operations[operator-1]} is {result}')
