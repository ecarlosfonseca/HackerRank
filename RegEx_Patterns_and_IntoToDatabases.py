import re

# Return names with gmail emails

if __name__ == '__main__':
    N = int(input())
    database = list()

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        database.append([firstName, emailID])

    pattern = re.compile(r'.+@gmail.com')
    unsorted_result = []
    for v in database:
        if pattern.match(v[1]):
            unsorted_result.append(v[0])
    [print(v) for v in sorted(unsorted_result)]
