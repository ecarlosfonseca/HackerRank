def superReducedString(s):
    S = list(s)
    while True:
        to_pop = []
        res = ''
        count = 0
        for i in range(len(S)):
            if i+count+1 <= len(S)-1:
                if S[i+count] == S[i+count+1]:
                    to_pop.append(i + count)
                    to_pop.append(i + count + 1)
                    count += 1
                else:
                    res += S[i]

        if len(to_pop) != 0:
            for j in range(len(to_pop)):
                S.pop(to_pop[j]-j)
        else:
            if res == '':
                return 'Empty String'
            else:
                res += S[-1]
                return res
            break

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s0 = 'aaabccddd'
    s1 = 'aa'
    s2 = 'baab'
    s3 = 'zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'

    result = superReducedString(s0)

    fptr.write(result + '\n')

    fptr.close()