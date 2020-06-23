def flatlandSpaceStations(n, c):

    if n == len(c):
        print(0)
    else:
        c = sorted(c)
        max_dist = max(c[0], n-1-c[-1])

        for i in range(len(c)-1):
            max_dist = max(max_dist, abs(c[i] - c[i+1])//2)

        print(max_dist)

if __name__ == '__main__':
    n0 = 5
    c0 = [0, 4]
    n1 = 6
    c1 = [0, 1, 2, 4, 3, 5]
    n2 = 20
    c2 = [13, 1, 11, 10, 6]
    flatlandSpaceStations(n2, c2)

