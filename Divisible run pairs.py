def divisible_sum_pairs(ar, k):

    # Count the number os pairs for which sum is a multiple os k

    count = 0
    for v in range(len(ar)):
        for i in range(len(ar)):
            if v != i and (ar[v] + ar[i]) % k == 0 and i >= v:
                print(ar[v], ar[i], ar[v] + ar[i])
                count += 1
    print(count)

if __name__ == '__main__':
    ar = [1, 3, 2, 6, 1, 2]
    k = 3
    divisible_sum_pairs(ar, k)

