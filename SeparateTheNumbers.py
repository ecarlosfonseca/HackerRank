def separateNumbers(s):

    for i in range(1, len(s)//2):
        strings = []
        sub_string = []
        j = 0
        first = True
        while j + i <= len(s):
            if not first:
                if sub_string[0] == '9' * i:
                    sub_string.append(s[j:j + i + 1])
                    j += i + 1
                else:
                    sub_string.append(s[j:j + i])
                    j += i
            else:
                sub_string.append(s[j:j + i])
                j += i
                first = False

        for j in range(len(sub_string)-1, 0, -1):
            if int(sub_string[j]) - int(sub_string[j-1]) != 1:
                break
            print('YES' + ' ' + sub_string[0])
            break


if __name__ == '__main__':
    s0 = '99910001001'
    s1 = '7891011'
    s2 = '9899100'
    separateNumbers(s1)
