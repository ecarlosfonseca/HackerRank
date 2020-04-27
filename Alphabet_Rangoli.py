def print_rangoli(n):

    # Prints Rangoli alphabet pattern with dimension n

    if n == 1:
        print('a')
    else:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


        width = 2*n + 2*(n-1)-1

        s_down = [str(alphabet[n-1])]
        s_up = []

        for i in range(n-1):
            s_down.append(s_down[-1] + '-' + f'{alphabet[n-2-i]}')

        for v in s_down:
            s_up.append('-' + v[::-1])

        print(s_down[0].center(width, '-'))
        for i in range(1, n):
            print((s_down[i] + s_up[i-1]).center(width, '-'))

        for i in range(n-2, 0, -1):
            print((s_down[i] + s_up[i-1]).center(width, '-'))
        print(s_down[0].center(width, '-'))

if __name__ == '__main__':
    n = 26
    print_rangoli(n)