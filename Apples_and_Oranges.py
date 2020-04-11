s, t = 7, 11
a, b = 5, 15
m, n = 3, 2
da = [-2, 2, 1]
do = [5, -6]

a_count = 0
o_count = 0

for d in da:
    if a + d in range(s, t+1):
        a_count += 1

for d in do:
    if b + d in range(s, t+1):
        o_count += 1

print(a_count)
print(o_count)


