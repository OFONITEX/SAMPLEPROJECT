# --------------------------------------
# operations supported by timedelta
# --------------------------------------

from datetime import timedelta

t1 = timedelta(days=5)
t2 = timedelta(days=20)

t3 = t1 + t2

t3 = t1 - t2      # or t2 - t1

t3 = t1 * 10      # or any integer
t3 = t1 / 10      # or any integer

t3 = t1 * 10.0    # or any float
t3 = t1 / 10.0    # or any float 

t3 = t2/t1        # result is a float and not timedelta

# https://docs.python.org/3/library/datetime.html#datetime.