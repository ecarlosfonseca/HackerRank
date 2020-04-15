def jumpingOntheClouds(c):

    # Returns minimum number of steps of 1 or 2 units necessary to complete path on the array
    # Can only walk on zero numbered values

    cloud = 0
    steps = 0
    while cloud < len(c)-1:

        if cloud + 2 <= len(c)-1 and c[cloud + 2] != 1:
            cloud += 2
            steps += 1
        elif cloud + 1 <= len(c)-1 and c[cloud + 1] != 1:
            cloud += 1
            steps += 1

    return steps

if __name__ == '__main__':
    c = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    print(jumpingOntheClouds(c))
