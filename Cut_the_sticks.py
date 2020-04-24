def cutTheSticks(arr):

    # returns array length in between steps of iterative process of removing the minimum value and subtracting it
    # to the remaining values until the array is empty

    result = []
    while len(arr) > 0:
        result.append(len(arr))
        n = min(arr)
        arr = list(filter(lambda a: a != n, arr))
        for v in arr:
            v -= n

    return result


if __name__ == '__main__':
    arr0 = [5, 4, 4, 2, 2, 8]
    print(cutTheSticks(arr0))