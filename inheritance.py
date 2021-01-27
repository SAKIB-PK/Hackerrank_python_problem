class Supercalculator:
    """Do addition , subtraction, Multiplication, division"""
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "It is impossible to divided by zero"
class Supercalculator(Calculator):
    def square(self,a):
        return a*a
    def cube(self,a):
        return pow(a,3)
my_calculator=Supercalculator()
print(my_calculator.addition(32,3))
my_calculator.square(33)


