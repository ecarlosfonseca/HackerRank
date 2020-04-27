def doorMat(N):

    """
    Prints  the following pattern for given N  (Size: N x 3N)
    Size: 7 x 21
        ---------.|.---------
        ------.|..|..|.------
        ---.|..|..|..|..|.---
        -------WELCOME-------
        ---.|..|..|..|..|.---
        ------.|..|..|.------
        ---------.|.---------
    """

    for i in range(N//2):
        print(('.|.'*(2*i+1)).center(3*N, '-'))
    print('WELCOME'.center(3*N, '-'))
    for i in range(N//2, 0, -1):
        print(('.|.'*(2*i-1)).center(3*N, '-'))


if __name__ == '__main__':
    N = 99
    doorMat(N)