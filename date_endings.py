import time
from datetime import datetime

date = raw_input('date: ')

if date[-2] == '0':
    date = date[1:]

st = '1'
nd = '2'
rd = '3'
th = ['4', '5', '6', '7', '8', '9', '0']

if len(date) == 1:
    if date == st:
        date += 'st'
    elif date == nd:
        date += 'nd'
    elif date == rd:
        date += 'rd'
    else:
        date += 'th'
elif len(date) == 2:
    if date[-2] == '1':
        date += 'th'
    else:
        if date[-1] == st:
            date += 'st'
        elif date[-1] == nd:
            date += 'nd'
        elif date[-1] == rd:
            date += 'rd'
        else:
            date += 'th'

print date
