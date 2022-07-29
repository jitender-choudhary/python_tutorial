lst = []
a = int(input('enter first num'))
d = int(input('enter the common difference'))
n = int(input('enter the number of terms'))

lst.append(a)

for i in range(1,n):
    a = a + d
    lst.append(a)
   
print(lst)
arithmatic_series = sum(lst)
print(arithmatic_series)
     
