'''Problem 19 Counting Sundays
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
if __name__ == "__main__":
    num_sundays = 0
    
    #Set up days
    days = dict()
    days[1] = 31
    days[1.1] = 31
    days[2] = 28
    days[2.1] = 29 #leap year
    days[3] = 31
    days[4] = 30
    days[5] = 31
    days[6] = 30
    days[7] = 31
    days[8] = 31
    days[9] = 30
    days[10] = 31
    days[11] = 30
    days[12] = 31

    #Sets up the rest of the leap year months
    for i in range(3, 13):
        days[i + 0.1] = days[i]
        
    day = 1 #Keep track of the day

    #This sets up the first sunday
    day += 6

    #Interate through years 1901 to end of 1999 
    #This is because 2000 is the only year that is divisible by 4 but is divisible by 400 (not a leap year)
    for year in range(1901, 2000):

        #This is a leap year
        if (year % 4 == 0):
            leap_indicator = 0.1
        
        #Not a leap year
        else:
            leap_indicator = 0
            
        month = 1 #Keep track of month
        
        #Check all sundays
        while (month < 13):
            
            #If we have found the first day is a sunday
            if (day == 1):
                num_sundays += 1
                
            day += 7
            
            #check to see if we need to proceed to the next month
            if (day > days[month + leap_indicator]):
                day = day - days[month + leap_indicator]
                month += 1
                
    #___          
    #Do the same thing for 2000 - not a leap year
    leap_indicator = 0
         
    month = 1 #Keep track of month
     
    #Check all sundays
    while (month < 13):
         
        #If we have found the first day is a sunday
        if (day == 1):
            num_sundays += 1
                 
            day += 7
             
        #check to see if we need to proceed to the next month
        if (day > days[month + leap_indicator]):
            day = day - days[month + leap_indicator]
        month += 1
        
    print "The number of sundays that fall in the first day of the month is: ", num_sundays