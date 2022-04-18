#---------------------------------
# python date arithmetic
#---------------------------------

from datetime import date, time, datetime, timedelta

# subtraction of dates
date1 = date(2017, 11, 20)
date2 = date(2017, 11, 10)

date1 - date2

# subtraction of datetime

date1 = datetime(2017, 11, 20, 1)
date2 = datetime(2017, 11, 10)

date1 - date2

# Duration in date terms, difference, interval
one_day = timedelta(days =1)
date1  = date1 + one_day

one_month = timedelta(days=30)

# check if date is within one month of today
# for statements, reminders
t_date = datetime(2021, 12, 21)

today = datetime.today()

if (today - t_date) <= one_month:
    print("True")
    
else:
    print("False")
    
# timedelta(days=0,
#           seconds=0,
#           microseconds=0,
#           milliseconds=0,
#           minutes=0,
#           hours=0,
#           weeks=0)


# multiplication of timedelta
one_month * 10

# division of timedelta
one_month /10

one_month /12
    
    30/12
    
    12*60*60
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    