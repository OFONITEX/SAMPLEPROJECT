# --------------------------------------------
# methods and functions of date 
# --------------------------------------------
from datetime import date

date1 = date(2017, 10, 25)

# replace method
date1.replace(year=2018)  # dates are immutable

date1 = date1.replace(year=2018)

# str for converting date to string
str(date1)

# ISO format date
date.isoformat(date1)

# string ( ISO format) to date)
date_str = str(date1)

date_iso = date.fromisoformat(date_str)


# weekday 1-Monday
date1.isoweekday()








