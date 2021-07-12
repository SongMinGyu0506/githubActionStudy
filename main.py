class Calculator:
    def add(self, num1,num2):
        return num1 + num2
    def subtract(self,num1,num2):
        return num2 - num1
    def mul(self, num1, num2):
        return num1 * num2
    def div(self,num1,num2):
        return num1 / num2

c = Calculator()
print(c.add(1,2))