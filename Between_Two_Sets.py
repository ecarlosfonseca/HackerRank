def between_two_sets(a, b):

    # Given two arrays a and b, it returns the count of numbers in between the two arrays are multiple os the elements
    # of the first array and divisors of the second array

    x = a[-1]
    y = b[0]
    b_div = []
    a_mult = []

    for i in range(x, y+1):
        count1 = 0
        for v in b:
            if v % i == 0:
                count1 += 1
                if count1 == len(b):
                    b_div.append(i)

        count2 = 0
        for val in a:
            if i % val == 0:
                count2 += 1
                if count2 == len(a):
                    a_mult.append(i)

    final = a_mult + b_div
    result = len(final) - len(set(final))

    return (result)

if __name__ == '__main__':
    a = [2, 4]
    b = [16, 32, 96]
    print(between_two_sets(a, b))
