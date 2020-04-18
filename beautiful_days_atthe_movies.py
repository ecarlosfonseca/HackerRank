def beautifulDays(i, j, k):

    # Returns number of differences between an integer and its reverse in given range, which are multiples of k

    beautiful = 0
    for number in range(i, j+1):
        rev_number = int(str(number)[::-1])
        if abs(rev_number - number) % k == 0:
            beautiful += 1

    return beautiful


if __name__ == '__main__':
    min_range = 20
    max_range = 23
    c = 6
    print(beautifulDays(min_range, max_range, c))