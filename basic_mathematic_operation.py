class Basic_operation :

    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2


    def addition(self):
        return  num1 + num2

    def multiplication(self):
        return  num1 * num2

    def subtraction(self):
        return num1-num2

    def divison(self):
        return num1/num2

num1 = 20
num2 = 10
x = Basic_operation(num1,num2)
option  = 1
while option != 0:
    print("0. For Exit")
    print("1. For Addition of given two numbers", num1, ',', num2)
    print("2. For Subtraction of given two numbers", num1, ',', num2)
    print("3. For Multiplication of given two numbers", num1, ',', num2)
    print("4. For Division of given two numbers", num1, ',', num2)
    option = int(input("Enter the option/choice you want = "))
    if option == 1:
        print("the addition of 20 and 10 is :", num1, ",", num2,"=" ,x.addition())

    elif option == 2:
        print("the multiplication of 20 and 10 is :", num1, ",", num2, ",", x.multiplication())
    elif option == 3:
        print("the subtraction of 20 and 10 is :", num1, ",", num2, ",", x.subtraction())
    elif option == 4:
        print("the divison  of 20 and 10 is :", num1, ",", num2, ",", x.divison())
    elif option == 0:
        print("exit the program")
    else:
        print("enter the choice again ")