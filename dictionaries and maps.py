if __name__ == '__main__':

    n = int(input())
    phone = dict()

    for _ in range(n):
        entry = input().split()
        phone[str(entry[0])] = str(entry[1])

    while True:
        try:
            query = input()

            try:
                result = f'{query}={phone[query]}'
            except:
                result = 'Not found'

            print(result)

        except:
            break