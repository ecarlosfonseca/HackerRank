def jorneyToMoon(n, astronaut):

    by_country = []
    by_country.append(set(astronaut[0]))

    for i in range(1, len(astronaut)):
        for country in by_country:
            if astronaut[i][0] in country or astronaut[i][1] in country:
                country.add(astronaut[i][0])
                country.add(astronaut[i][1])
                break

            else:
                by_country.append(set(astronaut[i]))
                break
    print(by_country)

    new = []
    for i in range(len(by_country)):
        for j in range(1, len(by_country)):
            big = by_country[i] | by_country[j]
            if len(big) != len(by_country[i]):
                for x in new:
                    if len(x|big)
                new.append(big)
            else:
                new.append(by_country[i])
                new.append(by_country[j])



    for i in range(n):
        out = True
        for country in by_country:
            if i in country:
                out = False
                break
        if out is True:
            new_country = set()
            new_country.add(i)
            by_country.append(new_country)

    if len(by_country) == 1:
        return len(by_country)-1
    else:
        result = 1
        for v in by_country:
            if len(v) != 1:
                result *= len(v)
            else:
                result += result - 1


    print(new)

if __name__ == '__main__':
    number_of_astronauts0 = 5
    line_up0 = [[0, 1], [2, 3], [0, 4]]  # 6
    number_of_astronauts1 = 4
    line_up1 = [[0, 2]]  # 5
    number_of_astronauts01 = 10
    line_up01 = [[0, 2], [1, 8], [1, 4], [2, 8], [2, 6], [3, 5], [6, 9]]  # (0, 1, 2, 4, 6, 8, 9) (7) (3, 5)
    number_of_astronauts02 = 100
    line_up02 = [[0, 11], [2, 4], [2, 95], [3, 48], [4, 85], [4, 95], [5, 67], [5, 83], [5, 42],[6, 76], [9, 31],
                    [9, 22], [9, 55], [10, 61], [10, 38], [11, 96], [11, 41], [12, 60],[12, 69], [14, 80], [14, 99],
                    [14, 46], [15, 42], [15, 75], [16, 87], [16, 71], [18, 99], [18, 44], [19, 26], [19, 59], [19, 60],
                    [20, 89], [21, 69], [22, 96], [22, 60], [23, 88], [24, 73], [27, 29], [30, 32], [31, 62], [32, 71],
                    [33, 43], [33, 47], [35, 51], [35, 75], [37, 89], [37, 95], [38, 83], [39, 53], [41, 84], [42, 76],
                    [44, 85], [45, 47], [46, 65], [47, 49], [47, 94], [50, 55], [51, 99], [53, 99], [56, 78], [66, 99],
                    [71, 78], [73, 98], [76, 88], [78, 97], [80, 90], [83, 95], [85, 92], [88, 99], [88, 94]]
    (jorneyToMoon(number_of_astronauts01, line_up01))