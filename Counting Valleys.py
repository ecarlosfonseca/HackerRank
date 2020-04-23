def counting_valleys(s):

    level = 0
    valleys = 0
    for i in s:
        if i == 'D':
            level += -1
            if level == -1:
                valleys += 1
        else:
            level += 1
    return valleys

if __name__ == '__main__':
    s = 'UDDDUDUU'
    print(counting_valleys(s))