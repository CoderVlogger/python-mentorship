class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def div(self):
        if self.y == 0:
            print('Division by zero!')
        else:
            return self.x / self.y
