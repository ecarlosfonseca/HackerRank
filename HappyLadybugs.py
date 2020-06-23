def happyLadybugs(b):

    if '_' not in b:
        if len(b) == 1:
            return 'NO'
        elif b[0] != b[1] or b[-1] != b[-2]:
            return 'NO'
        else:
            for i in range(1, len(b)-1):
                if b[i] != b[i+1] and b[i] != b[i-1]:
                    return 'NO'
    else:
        for char in b:
            if char.isalpha():
                if b.count(char) == 1:
                    return 'NO'
                    break
    return 'YES'


if __name__ == '__main__':

    b0 = ['G']
    print(happyLadybugs(b0))

