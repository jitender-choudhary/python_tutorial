class ListOperation:
    given_list = []


    def append_element(self, element):
        return self.given_list.append(element)


    def remove_element(self, element):
        return self.given_list.remove(element)
    def display_list(self):
        return self.given_list

x = ListOperation()
option = 1
while option != 0:
    print("Enter [0] to Exit the program")
    print("Enter [1] to Add element to the given list")
    print("Enter [2] to remove element from the given list")
    print("Enter [3] to print all the elements of the given list")
    option = int(input("Enter some random choice from 0 to 3 = "))
    if option == 1:
        element = int(input("enter some random number to be appended to the given_list"))
        x.append_element(element)
        print("The modified list after adding the elements to the list is : ", x.display_list())
    elif option == 2:
        element = int(input("enter some random number to be removed from  the given_list"))
        x.remove_element(element)
        print("The modified list after removing  the elements from  the list is : ", x.display_list())
    elif option == 3:

        print("The given list : \n", x.display_list())
    elif option == 0:
        print("Exit of program")
    else:
        print("The choice entered by user is invalid")