from datetime import datetime, timedelta

print(datetime.today()) # return current date and time.
datetime.today().date() # current date without time
datetime.today().time() # current time without date

#datetime.strptime(date_string, format) # return a datetime corresponding to date_string, parsed according to format.
# Format example: '%Y-%m-%d' - '2020-04-24'
mes = 5
def elegirmes(mes):
    pass

today = datetime.today()
today.day # the day of a current month.
today.strftime('%b') # the short name of the current month. I.e 'Apr'
today.weekday() # return the day of the week as an integer, where Monday is 0 and Sunday is 6.

yesterday = today - timedelta(days=1) # a timedelta object represents a duration, the difference between two dates or times.
day_after_tomorrow = today + timedelta(days=2)

import datetime

#get current time
d = datetime.datetime.now()

#print date
print(d)

#get month number
print(d.strftime("%m"))

#get current time
d = datetime.datetime.now()

#print date
print(d)

#get month number
x = d.strftime("%m")
print(x)
print(type(x))
if x == 5:
    print("Yikes")