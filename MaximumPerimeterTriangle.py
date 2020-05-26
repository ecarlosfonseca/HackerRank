def maximumPerimeterTriangle(sticks):

    # Selects maximum perimeter, non degenerate triangle from array of sides lengths

    if len(set(sticks)) == 1:
        return '' + str(sticks[0]) + ' ' + str(sticks[0]) + ' ' + str(sticks[0])
    else:
        valid_triangles = []
        for i in range(len(sticks) - 2):
            for j in range(i + 1, len(sticks) - 1):
                for k in range(j + 1, len(sticks)):
                    if sticks[i] + sticks[j] > sticks[k] and sticks[i] + sticks[k] > sticks[j] and sticks[j] + \
                            sticks[k] > sticks[i]:
                        valid_triangles.append(sorted([sticks[i], sticks[j], sticks[k]]))
        if len(valid_triangles) == 1:
            return '' + str(valid_triangles[0][0]) + ' ' + str(valid_triangles[0][1]) + ' ' + str(valid_triangles[0][2])
        elif len(valid_triangles) == 0:
            return -1
        else:
            perimeters = [sum(x) for x in valid_triangles]
            valid_triangles_max_per = []

            for i in range(len(valid_triangles)):
                if sum(valid_triangles[i]) == max(perimeters):
                    valid_triangles_max_per.append(valid_triangles[i])

            if len(valid_triangles_max_per) == 1:
                return '' + str(valid_triangles_max_per[0][0]) + ' ' + str(valid_triangles_max_per[0][1]) + ' ' \
                   + str(valid_triangles_max_per[0][2])
            else:
                max_lenghts = [max(v) for v in valid_triangles_max_per]
                valid_triangle_max_per_max_stick = []

                for i in range(len(valid_triangles_max_per)):
                    if max(valid_triangles_max_per[i]) == max(max_lenghts):
                        valid_triangle_max_per_max_stick.append(valid_triangles_max_per[i])

                if len(valid_triangle_max_per_max_stick) == 1:
                    return '' + str(valid_triangle_max_per_max_stick[0][0]) + ' ' + \
                       str(valid_triangle_max_per_max_stick[0][1]) + ' ' + str(valid_triangle_max_per_max_stick[0][2])
                else:
                    min_lengths = [min(v) for v in valid_triangle_max_per_max_stick]

                    for i in range(len(valid_triangle_max_per_max_stick)):
                        if min(valid_triangle_max_per_max_stick[i]) == min(min_lengths):
                            return '' + str(valid_triangle_max_per_max_stick[i][0]) + ' ' + str(
                            valid_triangle_max_per_max_stick[i][1]) + ' ' + str(valid_triangle_max_per_max_stick[i][2])
                        break
                    return '' + str(valid_triangle_max_per_max_stick[0][0]) + ' ' + \
                       str(valid_triangle_max_per_max_stick[0][1]) + ' ' + \
                       str(valid_triangle_max_per_max_stick[0][2])


if __name__ == '__main__':
    sticks0 = [1, 2, 3]
    sticks2 = [3, 9, 2, 15, 3]
    print(maximumPerimeterTriangle(sticks0))
