import math


def encryption(s):

    s = s.replace(' ', '')
    n = math.sqrt(len(s))

    if isinstance(n, int):
        width = int(math.sqrt(len(s))) + 1
    else:
        width = int(math.sqrt(len(s)))

    result = ''
    for i in range(width):
        aux = ''
        for v in range(i, len(s), width):
            aux += s[v]
            if len(aux) == width or v >= len(s) - width:
                result += aux + ' '

    return result[:-1]



if __name__ == '__main__':
    st = 'if man was meant to stay on the ground god would have given us roots'
    s0 = 'haveaniceday'
    s1 = 'feedthedog'
    s2 = 'chillout'
    s4 = 'iffactsdontfittotheorychangethefacts'
    s7 = 'wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny'

    print(encryption(s7))