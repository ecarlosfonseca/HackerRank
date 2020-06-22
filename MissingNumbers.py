def missingNumbers(arr, brr):

    b = brr.copy()
    for value in brr:
        if value in arr:
            b.remove(value)
            arr.remove(value)

    print(sorted(list(set(b))))


if __name__ == '__main__':

    arr0 = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
    brr0 = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

    missingNumbers(arr0, brr0)
