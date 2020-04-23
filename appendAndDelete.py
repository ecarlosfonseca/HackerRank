def appendAndDelete(s, t, k):

    # Determines if string t can be transformed in string s with k amount of appends() and or removes()

    cycles = min(len(s), len(t))
    for cycle in range(cycles):
        if s[cycle] != t[cycle]:
            stop = cycle
            break
        else:
            stop = len(s)

    moves = len(s) - stop + len(t) - stop

    if k == moves or k > moves and (k-moves) % 2 == 0 or k > moves and k > len(t) and k-len(t) > len(s):
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    st0 = 'hackerhappy'
    stt0 = 'hackerrank'
    k0 = 9
    st1 = 'aba'
    stt1 = 'aba'
    k1 = 7
    st2 = 'ashley'
    stt2 = 'ash'
    k2 = 2
    st5 = 'y'
    stt5 = 'yu'
    k5 = 2
    st10 = 'abcd'
    stt10 = 'abcdert'
    k10 = 10
    print(appendAndDelete(st10, stt10, k10))
