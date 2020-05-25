def workbook(n, k, arr):

    # Returns the number of problems with the same number as the page they are writen

    page = 1
    special = 0
    for v in arr:
        aux = 0
        print(aux, v//k)
        while aux <= v // k:
            if aux < v // k:
                for j in range(1, k+1):
                    print('a:', page, aux * k + j)
                    if aux * k + j == page:
                        special += 1
                        print(v, 'special1 + 1', special, page)
                    if j == k:
                        page += 1
                        aux += 1
            if aux == v//k and v % k == 0:
                break
            if aux == v//k:
                for j in range(1, v % k + 1):
                    print('b:', page, aux * k + j)
                    if aux * k + j == page:
                        special += 1
                        print(v, 'special2 + 1', special, page)
                    if j == v % k:
                        page += 1
                        aux += 1
    print(special)


if __name__ == '__main__':

    k0 = 3
    arr0 = [4, 2, 6, 1, 10]
    n0 = len(arr0)
    print(workbook(n0, k0, arr0))