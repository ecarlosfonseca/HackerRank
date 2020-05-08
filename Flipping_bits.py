def flippingBits(n):

    # Returns decimal flipped 32 bit binary of decimal n

    bin_n = str(bin(n))
    bin_32_n = bin_n[2:].zfill(32)

    # flipping binary digits
    f_bin_32_n = ''
    for v in bin_32_n:
        if v == '0':
            f_bin_32_n += '1'
        elif v == '1':
            f_bin_32_n += '0'

    return int(f_bin_32_n,2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
