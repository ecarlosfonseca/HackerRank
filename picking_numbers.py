def pickingNumbers(a):

    combos = []
    for value1 in range(len(a)):
        for value2 in range(len(a)):
            if abs(a[value1] - a[value2]) <= 1 and value1 < value2 and [a[value1], a[value2]] not in combos:
                combos.append([a[value1], a[value2]])
    biggest = 0
    for combo in combos:
        if combo[0] != combo[1] and a.count(combo[0]) + a.count(combo[1]) >= biggest:
            biggest = a.count(combo[0]) + a.count(combo[1])
        elif combo[0] == combo[1] and a.count(combo[0]) >= biggest:
            biggest = a.count(combo[0])

    return biggest



if __name__ == '__main__':
    arr = [4, 6, 5, 3, 3, 1]
    print(pickingNumbers(arr))