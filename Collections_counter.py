from collections import Counter

total_stock = int(input())
stock = list(map(int, input().split(' ')))
sizes = list(Counter(stock).keys())
availability = list(Counter(stock).values())
costumers = int(input())
transactions = []
business = 0
for i in range(costumers):
    transactions.append(list(map(int, input().split(' '))))

for transaction in transactions:
    for i in range(len(sizes)):
        if transaction[0] == sizes[i] and availability[i] > 0:
            availability[i] -= 1
            business += transaction[1]

print(business)

"""
input:  10
        2 3 4 5 6 8 7 6 5 18
        6
        6 55
        6 45
        6 55
        4 40
        18 60
        10 50
"""