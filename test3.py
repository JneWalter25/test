import datetime

vostok_1 = datetime.datetime(2021, 8, 5)
print(vostok_1)  # 1961-04-12 06:07:00
x = str(vostok_1)
y = x.split()
print(y[0])