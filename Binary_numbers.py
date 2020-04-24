def binary(n):

    # returns the number of consecutive ones in the binary representation o n

    binary = []
    counter = 0
    count = []

    while n != 0:
        if n % 2 == 0:
            binary.append(0)
            n = n//2
            if counter != 0:
                count.append(counter)
            counter = 0
        elif n % 2 == 1:
            binary.append(1)
            n = n//2
            counter += 1
    if counter != 0:
        count.append(counter)

    print(max(count))

if __name__ == '__main__':
    a = 13
    binary(a)