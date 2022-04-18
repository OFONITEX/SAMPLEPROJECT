#------------------------------
# datetime in python
#------------------------------

import datetime

date1 = datetime.date(2016, 7, 30)

year   = date1.year
month  = date1.month
day    = date1.day

# Not writeable
date1.year = 2019

# day out of range for month
year  = 2018
month = 11
day   = 31

date2 = datetime.date(year, month, day)

# create time variable 
time1 = datetime.time()  #default time format
print(time1)

time1 = datetime.time(13, 34, 40, 4000)
print(time1)

time1.hour
time1.minute
time1.second

# Get the date as well as the time
dt = datetime.datetime(2019, 10, 11, 15, 54, 39)

# Today
d1 = datetime.date.today()

d2 = datetime.datetime.today()








