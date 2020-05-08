def flippingBits(n):

    bin_n = bin(n)

    # adding left zeros so we have 32bit binary
    if len(str(bin_n)) < 32:
        bin_32_n = (32 - len(str(bin_n))) * '0' + str(bin_n).replace('b', '0')
    elif len(str(bin_n)) == 32:
        bin_32_n = str(bin_n).replace('b', '0')
    elif len(str(bin_n)) > 32:
        bin_32_n = str(bin_n).replace('0b', '')

    # flipping binary digits
    f_bin_32_n = ''
    for v in bin_32_n:
        if v == '0':
            f_bin_32_n += '1'
        elif v == '1':
            f_bin_32_n += '0'

    return bin_32_n# int(f_bin_32_n, 2)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #  q = int(input())

    #for q_itr in range(q):
    n = 4294967295

    print(flippingBits(n))

    #fptr.write(str(result) + '\n')

    #fptr.close()