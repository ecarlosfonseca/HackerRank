from itertools import groupby

def compressTheStringA(s):

    # Describe an input sequence with tuples (without imports)

    unique_chars = []
    unique_chars.append(s[0])
    count = 1
    for i in range(1, len(s)):
        if s[i] != unique_chars[-1]:
            unique_chars.append(count)
            unique_chars.append(s[i])
            count = 1
        else:
            count += 1
    if len(unique_chars) % 2 != 0:
        unique_chars.append(count)

    for j in range(0, len(unique_chars) - 1, 2):
        print((unique_chars[j + 1], int(unique_chars[j])), end=' ')


def compressTheStringB(s):

    # Describe an input sequence with tuples (with imports)

    groups = [(len(list(c)), int(s)) for s, c in groupby(s)]
    for group in groups:
        print(group, end=' ')

if __name__ == '__main__':
    s0 = '1222311'
    compressTheStringA(s0)
    print()
    compressTheStringB(s0)
