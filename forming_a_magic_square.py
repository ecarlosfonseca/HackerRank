"""
magic_squares =[
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

"""

def formingMagicSquare(s):

    # Calculates minimum changing cost for the transformation of s (3*3) into a magic square

    magic_squares = []

    for a1 in range(1, 9):
        for a2 in range(1, 9):
            for a3 in range(1, 9):
                for a4 in range(1, 9):
                    for a5 in range(1, 9):
                        for a6 in range(1, 9):
                            for a7 in range(1, 9):
                                for a8 in range(1, 9):
                                    for a9 in range(1, 9):
                                        if a1 + a2 + a3 == a4 + a5 + a6 == a7 + a8 + a9 == a1 + a4 + a7 == a2 + a5 + a8 == a3 + a6 + a9 == a1+a5+a9 == a3+a5+a7 == 15:
                                            magic_squares.append([a1, a2, a3, a4, a5, a6, a7, a8, a9])

    turning_costs = []
    for magic_square in magic_squares:
        turning_costs.append(abs(s[0][0]-magic_square[0]) + abs(s[0][1]-magic_square[1]) + abs(s[0][2]-magic_square[2]) + abs(s[1][0]-magic_square[3]) + abs(s[1][1]-magic_square[4]) + abs(s[1][2]-magic_square[5]) + abs(s[2][0]-magic_square[6]) + abs(s[2][1]-magic_square[7]) + abs(s[2][2]-magic_square[8]))

    return min(turning_costs)


if __name__ == '__main__':
    a = [
        [4, 8, 2],
        [4, 5, 7],
        [6, 1, 6]
    ]
    print(formingMagicSquare(a))
