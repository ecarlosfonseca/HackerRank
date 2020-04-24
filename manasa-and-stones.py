def stones(n, a, b):

    last_stone = [(n - 1) * a, (n - 1) * b]
    for i in range(n-1):
        last_stone.append((n-1-i) * a + i * b)

    return sorted(list(set(last_stone)))


if __name__ == '__main__':
    n1 = 3
    a1 = 1
    b1 = 2
    print(stones(n1, a1, b1))