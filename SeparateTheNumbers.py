def separateNumbers(s):

    p = False
    for i in range(1, len(s)//2+1):
        sub_string = []
        j = 0
        first = True
        l = 0

        while j + i <= len(s):
            if not first:
                if sub_string[-1] == '9' * i or len(sub_string[-1]) > i:
                    sub_string.append(s[j:j + i + 1])
                    l += len((s[j:j + i+1]))
                    j += i + 1
                else:
                    sub_string.append(s[j:j + i])
                    l += len((s[j:j + i]))
                    j += i

            else:
                sub_string.append(s[j:j + i])
                l += len((s[j:j + i]))
                j += i
                first = False

        if sum(map(int, sub_string)) == len(sub_string) * int(sub_string[0]) + sum(list(range(len(sub_string)))):
            if len(sub_string[0]) > 1 and int(sub_string[0][0]) == 0:
                pass
            elif int(sub_string[1]) - int(sub_string[0]) == 1 and len(s) % len(sub_string) == 0 and l == len(s):
                p = True
                print('YES' + ' ' + sub_string[0])

    if not p:
        print('NO')


if __name__ == '__main__':
    s0 = '99910001001'
    s1 = '7891011'
    s2 = '9899100'
    s3 = '999100010001'
    s4 = '99100'
    s5 = '010203'
    s6 = '4294967295429496729642949672'
    separateNumbers(s6)

