class StringClass:
    def __init__(self):
        self.string = " "

    def get_string(self):
        self.string = input("enter the string : ")
        print(type(self.string))


    def put_string(self):
        print("the string is",self.string)

string_object = StringClass()
string_object.get_string()
string_object.put_string()


