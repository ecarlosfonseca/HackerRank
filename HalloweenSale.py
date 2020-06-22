def howManyGames(p, d, m, s):

    games = 0
    while s - p >= 0:
        s -= p
        games += 1
        p = max(p-d, m)

    return games


if __name__ == '__main__':

    pdms0 = (20, 3, 6, 80)
    p0 = int(pdms0[0])
    d0 = int(pdms0[1])
    m0 = int(pdms0[2])
    s0 = int(pdms0[3])
    print(howManyGames(p0, d0, m0, s0))

    pdms1 = (20, 3, 6, 85)
    p1 = int(pdms1[0])
    d1 = int(pdms1[1])
    m1 = int(pdms1[2])
    s1 = int(pdms1[3])
    print(howManyGames(p1, d1, m1, s1))
