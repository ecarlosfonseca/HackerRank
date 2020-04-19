def circularArrayRotation(a, k, queries):

    rotated_a = a[len(a) - k: len(a) + 1]
    for v in range(len(a) - k):
        rotated_a.append(a[v])

    return rotated_a[queries]


if __name__ == '__main__':
    arr = [1, 2, 3]  # [2, 3, 1]
    rotations = 2
    keys = [0, 1, 2]
    for v in keys:
        print(circularArrayRotation(arr, rotations, v))
