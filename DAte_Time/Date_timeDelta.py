from datetime import datetime, timedelta, timezone

dt1 = datetime(2023, 8, 20)
dt2 = datetime.now()
duration = dt2-dt1
print(duration)
print("Days:", duration.days)
print("Sec:", duration.seconds)
