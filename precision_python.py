import math


class Precision :

    def __init__(self, num):
        self.num = num
    # precision using % operator
    def precision(self):
        return '%.4f' % self.num
    # precision using format function
    def precision_format(self):
        return '{0:.5f}' .format(self.num)
    # precision using round function
    def precision_round(self):
        return round(self.num,3)
    # precision using trunc function
    def precision_trunck(self):
        return math.trunc(self.num)
    # precision using ceil function
    def precision_ceil(self):
        return math.ceil(self.num)
    # precision using floor function
    def precision_floor(self):
        return math.floor(self.num)

x = Precision(20.34345678)
print(x.precision())
print(x.precision_format())
print(x.precision_round())
print(x.precision_trunck())
print(x.precision_floor())