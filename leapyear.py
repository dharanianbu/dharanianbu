year = int(input("Enter a year:"))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} leap year".format(year))  
       else:  
           print("{0} leap year".format(year))  
   else:  
       print("{0} leap year".format(year))  
else:  
   print("{0} leap year".format(year))  
