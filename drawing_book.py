def page_count(n, p):

    # Returns minimum number of pages to turn (1 by 1) on a book with n pages, to get to page p starting
    # from beginning or end

    if n % 2 == 0 and p % 2 != 0:
        return min(p//2, (n-p)//2+1)
    else:
        return min(p//2, (n-p)//2)


if __name__ == '__main__':
    n = 5
    p = 4
    print(page_count(n, p))

"""
even n, ex: 10
1 23 45 67 89 10

even p
beg: p//2
end: (n-p)//2

odd p
beg: p//2
end: (n-p)//2 + 1

od n, ex:13
1 23 45 67 89 1011 1213

even p
beg:  p//2
end: (n-p)//2

odd p
beg: p//2
end: (n-p)//2
"""