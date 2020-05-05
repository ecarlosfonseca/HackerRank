from collections import OrderedDict

d = {}
for i in range(int(input())):
    article = input().split()
    product = ''
    price = 0
    for v in article:
        if v.isdigit():
            price += int(v)
        else:
            product += v + ' '
    if product[:-1] not in d:
        d[product[:-1]] = int(price)
    else:
        d[product[:-1]] += price

for v in d:
    print(v, d[v])

""""
Input:
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
"""
