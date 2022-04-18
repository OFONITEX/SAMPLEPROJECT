#===============================================
# strftime - date    ---> string format
# strptime - string  ---> date format

# d - dd
# m - mm
# y - yy
# Y - yyyy

# H - hh
# M - mm
# S - ss
#
# a - three letter weekday
# A - full name of the weekday
# W - day number starting from Monday
#
# b - Three letter month
# B - full name of the month
# m - month number
# p - PM
# ==============================================
from datetime import datetime

date1 = datetime(2017, 11, 10, 21, 45, 19)

str(date1)

# dd-mm-yyyy format
datetime.strftime(date1, '%d')
datetime.strftime(date1, '%m')
datetime.strftime(date1, '%Y')

datetime.strftime(date1, '%d/%m/%Y')

# HH:MM:SS
datetime.strftime(date1, '%H:%M:%S')

# Weekday

d_a = datetime.strftime(date1, '%a')
d_A = datetime.strftime(date1, '%A')
d_w = datetime.strftime(date1, '%w')


# 12 hour time
datetime.strftime(date1, '%I:%M:%S')

datetime.strftime(date1, '%I:%M:%S %p')   # for pm time use small letter p


# strptime
date2_str = '19/06/2018'

date2_d   = datetime.strptime(date2_str,  '%d/%m/%Y')








