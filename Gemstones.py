def gemstones(arr):

    # Returns common elements to all string elements of an array

    composition = []
    for element in set(arr[0]):
        composition.append([element, 1])

    for rock in arr[1:]:
        for element in composition:
            if element[0] in rock:
                element[1] += 1

    gemstone_counter = 0
    for v in composition:
        if v[1] == len(arr):
            gemstone_counter += 1

    return gemstone_counter



if __name__ == '__main__':
    arr0 = ['abcdde', 'baccd', 'eeabg']
    print(gemstones(arr0))

