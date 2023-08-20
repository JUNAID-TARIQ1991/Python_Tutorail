from datetime import datetime
import time
dt1 = datetime(2010, 1, 12)  # datetime object
print(dt1.now())

print(dt1)

# string to date time object, using directives
dt = datetime.strptime("2023/08/01", "%Y/%m/%d")
print(dt)
dt = datetime.fromtimestamp(time.time())  # using time module
print(dt)
dt = dt.strftime("%Y,%M")  # Date time to string
print(type(dt))
