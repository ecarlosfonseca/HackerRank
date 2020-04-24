def libraryFine(d1, m1, y1, d2, m2, y2):

    # calculates library fine for late delivery, 15/day, 500/month, 10000/year. These do not add together.

    if y2 < y1:
        return 10000
    elif m2 < m1 and y2 == y1:
        return 500*(m1-m2)
    elif d2 < d1 and m2 == m1 and y2 == y1:
        return 15*(d1-d2)
    else:
        return 0


if __name__ == '__main__':
    da, ma, ya = 6, 6, 2015  # returned date  45
    db, mb, yb = 9, 6, 2016  # due date
    print(libraryFine(da,ma,ya,db,mb,yb))