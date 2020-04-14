def migratory_birds(ar):

    # returns the most common occurrence in a list

    types = sorted(list(set(ar)))
    max = 0
    winner = ()
    for type in types:
        aux = ar.count(type)
        if aux > max:
            max = aux
            winner = (type, max)

    print(winner[0])

if __name__ == '__main__':
    ar = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
    migratory_birds(ar)
