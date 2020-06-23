def closestNumbers(arr):

    # Returns min dif between two elements of an array

    pairs = []
    arr = sorted(arr)
    difs = []
    for i in range(len(arr)-1):
        pairs.append([arr[i], arr[i+1]])
        difs.append(abs(arr[i+1]-arr[i]))

    result = []
    a = min(difs)
    for i in range(len(difs)):
        if difs[i] == a:
            result.append(pairs[i][0])
            result.append(pairs[i][1])

    return result


if __name__ == '__main__':

    arr0 = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854 ]
    print(closestNumbers(arr0))

