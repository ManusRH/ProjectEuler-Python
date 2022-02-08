"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.

All the rest have thirty-one,

Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

1901 jan 1 = tuesday
"""

months = {
'a-jan' : 31,
'b-feb' : 28,  #leap years = 29
'c-mar' : 31,
'd-apr' : 30,
'e-may' : 31,
'f-jun' : 30,
'g-jul' : 31,
'h-aug' : 31,
'i-sep' : 30,
'j-octo' : 31,
'k-nov' : 30,
'l-dec' : 31
}

#       mo,tu,we,th,fr,sa,su
days = [1, 2, 3, 4, 5, 6, 7] 

sundays_1st = []

which_day = 0


def sunday_on_1st(year):
    if year == 1900:
        months['b-feb'] = 28
    elif year % 4 == 0:
        months['b-feb'] = 29
    else:
        months['b-feb'] = 28

    global which_day

    for key, value in sorted(months.items()):
        month = range(0,value)
        append_if = []
        for day in month:
            which_day += 1
            append_if.append(which_day)
            if which_day > 6:
                which_day = 0
        if append_if[0] == 7 and year != 1900:
            sundays_1st.append("sunday!")

for year in range(1900,2001): #find sundays in year 1900 (makes it easier)
    sunday_on_1st(year)

print(len(sundays_1st))
