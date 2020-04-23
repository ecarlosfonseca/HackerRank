def apples_and_oranges(s, t, a, b, apples, oranges):

    # Calculates the number of elements from arr apples and arr oranges with relative position to a and b
    # are in the s, t range. s and t are absolute

    a_count = 0
    o_count = 0

    for d in apples:
        if a + d in range(s, t+1):
            a_count += 1

    for d in oranges:
        if b + d in range(s, t+1):
            o_count += 1

    print(a_count)
    print(o_count)

if __name__ == '__main__':
    s1 = 7
    t1 = 11
    a1 = 5
    b1 = 15
    apples1 = [-2, 2, 1]
    oranges1 = [5, -6]
    apples_and_oranges(s1, t1, a1, b1, apples1, oranges1)
