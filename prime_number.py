class Prime:
    def __init__(self,num):
        self.num = num

    def check_if_prime(self):
        for i in range(2,self.num-1):
            if (self.num % i) == 0:
                print("the given number is not a prime number")
                break
        else:
            print("the given number is prime")

x = int(input("enter the number : "))
prime = Prime(x)
prime.check_if_prime()