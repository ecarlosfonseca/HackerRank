"""
Converte horas no formato 12 (AM/PM) no formato 24

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
      Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
"""

s = '12:00:00PM'

hour = s[0]+s[1]
if s[-2] == 'P':
    if int(hour) == 12:
        print(s[:-2])
    else:
        hour = int(hour) + 12
        print(str(hour) + s[2:-2])
elif int(hour) == 12:
    print('00' + s[2:-2])
else:
    print(s[:-2])

"""
time = string.strip()
    h, m, s = map(int, time[:-2].split(':'))
    time_format = time[-2:]
    h = h % 12 + (time_format.upper() == 'PM') * 12
    return ('%02d:%02d:%02d') % (h, m, s)
"""