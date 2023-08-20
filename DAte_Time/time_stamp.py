import time


def send_email():
    for i in range(1000):
        print(i)


start = time.time()
send_email
stop = time.time()
duration = stop-start
print(duration)
