
def add(x, y):
    return x + y

print("Choice operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Operation: ")

x = int(input("Enter X: "))
y = int(input("Enter Y: "))

if operation == 1:
    r = add(x, y)
elif operation == 2:
    r = x - y

elif operation == 3:
    r = x * y

elif operation == 4:
    r = x / y

print("Result: ", r)
