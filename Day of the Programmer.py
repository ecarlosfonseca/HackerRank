def dayOfprogrammer(y):

    # returns the 256th day of a given year in Russia

    if y <= 1917:
        if y % 4 == 0:
            return f'12.09.{y}'
        else:
            return f'13.09.{y}'
    elif year == 1918:
        return f'26.09.{y}'
    else:
        if y % 400 == 0:
            return f'12.09.{y}'
        elif y % 4 == 0 and y % 100 != 0:
            return f'12.09.{y}'
        else:
            return f'13.09.{y}'

if __name__ == '__main__':
    y = 1800
    print(dayOfprogrammer(y))