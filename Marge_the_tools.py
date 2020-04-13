def merge_the_tools(s, k):

    for i in range(0, len(s), k):
        st = s[i: i + k]
        print("".join(dict.fromkeys(st)))

if __name__ == '__main__':
    s = 'AABCAAADA'
    k = 3
    merge_the_tools(s, k)