def toys(w):

    w.sort()
    containers = [[w[0]]]

    for i in range(1, len(sorted(w))):
        v = w[i]
        check = False
        for container in containers:
            if v - container[0] <= 4:
                container.append(v)
                check = True
        if not check:
            containers.append([v])

    print(containers)
    print(len(containers))


if __name__ == '__main__':

    w0 = [1, 2, 3, 21, 7, 12, 14, 21]
    w1 = [12, 15, 7, 8, 19, 24]
    w3 = [88, 34, 99, 23, 30, 84, 56, 37, 5, 55]
    # [5] [84, 88] [30, 34] [99], [23] [55, 56] [37
    toys(w3)
