def minimumDistances(a):

    # returns te minimum distance between two equal elements in array a

    indexes = []
    no_reps = set(a)
    for v in no_reps:
        if a.count(v) != 0:
            index = []
            for i in range(len(a)):
                if a[i] == v:
                    index.append(i)
            indexes.append(index)

    distances = []
    for index in indexes:
        if len(index) > 1:
            distance = abs(index[0]-index[1])
            distances.append(distance)

    return min(distances) if len(distances) != 0 else -1



if __name__ == '__main__':
    arr = [1, 2, 3, 4, 10]
    print(minimumDistances(arr))