class Area:


    def __init__(self,radius):
        self.radius = radius

    def calculate_perimeter(self):
        r = (self.radius)
        return 2*3.14*r

    def calculate_area(self):
        r = (self.radius)
        return 3*r*r

rad = float(input("enter the radius of the circle  :"))

area = Area(rad)
circle_perimeter = area.calculate_perimeter()
circle_area = area.calculate_area()
print("area of circle is :",circle_area)
print("perimeter of the circle is :",circle_perimeter)

