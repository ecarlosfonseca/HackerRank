from collections import defaultdict

ns = input().split(' ')
n = int(ns[0])
m = int(ns[1])
d = defaultdict(list)

for i in range(1, n+1):
    d[input()].append(i)

for v in range(m):
    B = input()
    if B in d:
        print(" ".join(map(str, d[B])))
    else:
        print(-1)
