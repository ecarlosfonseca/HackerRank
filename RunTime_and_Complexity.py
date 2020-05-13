def is_prime(n):

    # Returns if a number is prime or not

    if n == 1:
        return 'Not prime'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 'Not prime'
    return 'Prime'


if __name__ == '__main__':
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 907]
    for j in range(len(a)):
        number = a[j]
        print(is_prime(number))


