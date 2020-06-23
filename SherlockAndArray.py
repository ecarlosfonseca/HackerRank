def balancedSums(arr):

    total = sum(arr)
    s = 0
    for value in arr:
        if s == total-value-s:
            return "YES"
        s += value
    return "NO"


if __name__ == '__main__':
    arr = [1, 1, 4, 1, 1,]
    balancedSums(arr)
