def saveThePrisoner(n, m, s):

    a = s + m - 1
    if a > n:
        if a % n == 0:
            return n
        else:
            return a % n;
    else:
        return a


if __name__ == '__main__':
    prisoners = 559033664
    pieces = 822024089
    start = 131746755
    print(saveThePrisoner(prisoners, pieces, start))




