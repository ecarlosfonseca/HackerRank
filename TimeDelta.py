from datetime import datetime as dt, timedelta

def time_delta(t1, t2):

    date_format = '%a %d %b %Y %H:%M:%S %z'

    solution = abs(dt.strptime(t1, date_format) - dt.strptime(t2, date_format))

    print(int(solution.total_seconds()))


if __name__ == '__main__':
    t10 = 'Sun 10 May 2015 13:54:36 -0700'
    t20 = 'Sun 10 May 2015 13:54:36 -0000'
    time_delta(t10, t20)
