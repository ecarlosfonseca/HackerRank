import math


def squares(a, b):

    if (a**0.5).is_integer():
        result = 1
    else:
        result = 0

    n = (int(a**0.5) + 1)**2

    while n <= b:
        if n <= b:
            result += 1
            n += 2*(n**0.5)+1
        else:
            n += 2*(n**0.5)+1

    return result


if __name__ == '__main__':
    a1 = 3
    b1 = 9
    aa = 17
    bb = 24
    print(squares(a1,b1))