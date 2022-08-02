class Mydate:


    def string_from_num(self, num):
        self.num = num
        a = self.num
        b = str(a)
        if len(b) == 7:
            c = "0" + b
        else:
            c = b
        year = (c[4 : 8])
        date = (c[0 : 2])
        month = (c[2 : 4])
        month_int = (int(month))
        d = {1 : "January",
                  2 : "February",
                  3 : "March",
                  4 : "April",
                  5 : "May",
                  6 :"June",
                  7 :"July",
                  8 : "August",
                  9 : "September",
                  10 : "October",
                  11 : "November",
                  12 : "December"}
        month_string = d.get(month_int)
        print("Date in string format is {0} - {1} - {2} ".format(date, month_string, year))

    def num_from_string(self, num):
        self.num = num
        e = self.num
        f = e.split("-")
        print(f)
        date_s = f[0]
        year_s = f[2]
        month_s = f[1]
        monthint = month_s.capitalize()
        f = {"January" : "01",
                  "February" : "02",
                  "March"  : "03",
                  "April"  : "04",
                  "May"  : "05",
                  "June" : "06",
                  "July" : "07",
                  "August" : "08",
                  "September" : "09",
                  "October" : "10",
                  "November" : "11",
                  "December"  : "12"}
        month_in_int = f.get(monthint)
        date_number_from_string = date_s + month_in_int + year_s
        print("Date in integer format is {0}".format(date_number_from_string))


date_in_int = int(input("enter the date in ddmmyyyy format  :"))
date_in_string = input("enter the date in dd-month_in_string-year seperated by - :")

mydate = Mydate()
x = mydate.string_from_num(date_in_int)
y = mydate.num_from_string((date_in_string))









