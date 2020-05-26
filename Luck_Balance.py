def luckBalance(k, contests):

    # Returns the maximum luck level you can have in a problem sequence

    luck = 0
    important_contests = []
    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        else:
            important_contests.append(contest[0])

    if len(important_contests) == 0:
        print(luck)
    elif k >= len(important_contests):
        print(luck + sum(important_contests))
    else:
        if k == 0:
            print(luck - sum(important_contests))
        else:
            for _ in range(k):
                luck += max(important_contests)
                important_contests.remove(max(important_contests))

            print(luck - sum(important_contests))

if __name__ == '__main__':

    k0 = 3
    k1 = 99
    k2 = 100
    contests0 = [(5, 1), (2, 1), (1, 1), (8, 1), (10, 0), (5, 0)]
    contests1 = [(5351, 0), (1870, 0), (9359, 0), (6828, 0), (9896, 0), (6335, 0), (38, 0), (2440, 0), (4627, 0), (2663, 0), (6300, 0), (107, 0), (4605, 0), (5437, 0), (4394, 0), (7530, 0), (8254, 0), (5668, 0), (6945, 0), (1539, 0), (1323, 0), (1841, 0), (2191, 0), (8943, 0), (7645, 0), (3903, 0), (4772, 0), (2392, 0), (1539, 0), (7712, 0), (9955, 0), (9895, 0), (7422, 0), (4665, 0), (5448, 0), (2317, 0), (6963, 0), (9170, 0), (2860, 0), (3812, 0), (5725, 0), (1324, 0), (7377, 0), (5538, 0), (2383, 0), (7674, 0), (5142, 0), (3932, 0), (2624, 0), (8704, 0), (5706, 0), (2649, 0), (6730, 0), (8757, 0), (2930, 0), (4465, 0), (6119, 0), (4967, 0), (8717, 0), (334, 0), (9962, 0), (293, 0), (1943, 0), (8146, 0), (4085, 0), (779, 0), (9630, 0), (1843, 0), (289, 0), (2083, 0), (9742, 0), (5891, 0), (2996, 0), (7447, 0), (4371, 0), (1102, 0), (6501, 0), (492, 0), (3806, 0), (3549, 0), (9719, 0), (9913, 0), (9265, 0), (8468, 0), (5007, 0), (1479, 0), (2758, 0), (1727, 0), (5548, 0), (6869, 0), (154, 0), (42, 0), (6309, 0), (9041, 0), (3036, 0), (3282, 0), (4828, 0), (7036, 0), (8724, 0)]
    contests2 = [(437, 1), (68, 0), (319, 0), (565, 0), (307, 1), (512, 0), (493, 0), (30, 0), (557, 0), (367, 0), (547, 1), (263, 0), (481, 0), (78, 0), (492, 1), (56, 1), (81, 0), (154, 0), (503, 1), (375, 0), (152, 0), (401, 0), (226, 0), (482, 0), (264, 0), (52, 0), (9, 0), (145, 0), (72, 0), (293, 0), (15, 0), (42, 1), (305, 0), (34, 0), (509, 0), (156, 0), (321, 0), (437, 0), (510, 1), (449, 0), (79, 0), (492, 0), (191, 0), (354, 1), (529, 0), (315, 0), (384, 0), (371, 0), (100, 0), (480, 0), (408, 0), (221, 0), (286, 0), (551, 0), (106, 0), (123, 0), (549, 0), (183, 1), (428, 0), (435, 0), (370, 0), (46, 0), (289, 0), (246, 0), (414, 1), (159, 0), (442, 0), (286, 0), (21, 0), (119, 0), (263, 0), (572, 0), (334, 0), (96, 0), (307, 0), (323, 0), (554, 1), (487, 0), (455, 1), (399, 0), (559, 0), (276, 0), (357, 1), (586, 0), (346, 0), (240, 1), (492, 0), (63, 0), (262, 0), (489, 0), (124, 1), (526, 0), (350, 1), (243, 0), (35, 0), (292, 0), (418, 0), (364, 1), (41, 1), (519, 0)]
    luckBalance(k2, contests2)
