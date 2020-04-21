def permutationEquation(p):

    auxx = []
    for value in range(1, len(p)+1):
        for i in range(len(p)):
            if p[i] == value:
                auxx.append(i+1)

    solution = []

    for aux in auxx:
        for j in range(len(p)):
            if p[j] == aux:
                solution.append(j+1)

    return solution


if __name__ == '__main__':
    arr = [2, 3, 1]
    print(permutationEquation(arr))