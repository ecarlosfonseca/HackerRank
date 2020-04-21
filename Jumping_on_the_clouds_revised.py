def jumpingOnClouds(c, k):

    position = 0
    energy = 100
    end = False

    while end is False:
        position += k
        energy -= 1
        if c[position % len(c)] == 1:
            energy -= 2
        if position % len(c) == 0:
            end = True

    return energy


if __name__ == '__main__':
    path = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    jump_size = 3
    print(jumpingOnClouds(path, jump_size))