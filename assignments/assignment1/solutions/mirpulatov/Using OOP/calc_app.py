from calc import Calculator


while True:
    operation = input("Choose operation:\n"
                      "1. Sum\n"
                      "2. Subtract\n"
                      "3. Multiply\n"
                      "4. Divide\n"
                      "5. Exit\n")

    if operation == "5":
        break

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    calc = Calculator(a, b)

    if operation == "1":
        print("Sum of a and b = {0}".format(calc.plus()))
    elif operation == "2":
        print("Subtraction of a and b = {0}".format(calc.minus()))
    elif operation == "3":
        print("Multiplication of a and b = {0}".format(calc.multiply()))
    elif operation == "4":
        print("Division of a and b = {0}".format(calc.div()))
