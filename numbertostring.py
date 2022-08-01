class Mydate:


      def number_string(self, num):
            self.num = num
            a = str(self.num)
            year = (a[4:8])
            print(year)
            date = (a[0:2])
            print(date)
            month = (a[2:4])
            print(month)
            if month == "01":
                month_string = "january"
            elif month == "02":
                month_string = "february"
            elif month == "03":
                month_string = "march"
            elif month == "04":
                month_string = "april"
            elif month == "04":
                month_string = "may"
            elif month == "04":
                month_string = "june"
            elif month == "04":
                month_string = "july"
            elif month == "04":
                month_string = "august"
            elif month == "04":
                month_string = "september"
            elif month == "04":
                month_string = "october"
            elif month == "11":
                month_string = "november"
            elif month == "04":
                month_string = "december"
            print(month_string)
            month_format_string = date +  month_string +  year
            print(month_format_string)
            print("{0} - {1} - {2} ".format(date,month_string,year))
      def number_int(self, date, month, year):
            self.date = date
            self.month = month
            self.year = year
            c = {"January" : "01",
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
            d = self.month
            month_int =  c.get(d)
            print(month_int)
            print("{0} - {1} - {2} ".format(self.date, month_int, self.year))

         
          
x = Mydate()
x.number_string("03112021")
x.number_int('14', 'April', '1993')

    

