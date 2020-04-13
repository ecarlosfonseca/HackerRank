def birthday_chocolate(s, d, m):

    combs = []
    count = 0
    for i in range(len(s)):
        if i + m <= len(s):
            comb = s[i:i+m]
            combs.append(comb)

    for comb in combs:
        if sum(comb) == d:
            count += 1

    return count



if __name__ == '__main__':
    s = [1, 1, 1, 1, 1, 1]  # integers on each piece of chocolate
    d = 3  # sum to deliver
    m = 2  # number os pieces to deliver

    print(birthday_chocolate(s, d, m))