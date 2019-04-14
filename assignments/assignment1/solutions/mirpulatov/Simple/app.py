def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiply(x, y):
    return x * y


def div(x, y):
    return x / y


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

    if operation == "1":
        print("Sum of a and b = {0}".format(plus(a, b)))
    elif operation == "2":
        print("Subtraction of a and b = {0}".format(minus(a, b)))
    elif operation == "3":
        print("Multiplication of a and b = {0}".format(multiply(a, b)))
    elif operation == "4":
        print("Division of a and b = {0}".format(div(a, b)))
