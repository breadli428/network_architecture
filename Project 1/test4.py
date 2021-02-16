year = int(input('year = '))
month = int(input('month = '))
day = int(input('day = '))


def isleap(yy):
    if (yy % 4 == 0 and yy % 100 != 0) or yy % 400 == 0:
        flag = 1
    else:
        flag = 0
    return flag


mm = range(1, 13)
if isleap(year) == 1:
    feb = 29
else:
    feb = 28
dd = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

order = 0
for m in mm:
    if m < month:
        order += dd[m-1]
    else:
        order += day
        break

print('It is the %dth day of the year' % order)
