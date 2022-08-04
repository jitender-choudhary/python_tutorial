class Gcd:

    def calculate_gcd(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        if self.num1 > self.num2:
            smallnumber = num2
        else:
            smallnumber = num1
        for i in range(1,smallnumber+1):
            if (num1%i == 0) and (num2%i == 0):
                result = i
        return result

x = int(input("enter the first number : "))
y = int(input("enter the second number : "))
findgcd = Gcd()
ans = findgcd.calculate_gcd(x,y)
print("the gcd of given number is : ", ans)