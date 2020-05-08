def insertionSort1(arr):

    x = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        if x < arr[i-1]:
            arr[i] = arr[i-1]

            for j in range(len(arr)):
                if j == len(arr) - 1:
                    print(arr[j])
                else:
                    print(arr[j], end = ' ')
            if i-1 == 0:
                arr[0] = x
                for j in range(len(arr)):
                    if j == len(arr) - 1:
                        print(arr[j])
                    else:
                        print(arr[j], end = ' ')

        else:
            arr[i] = x
            for j in range(len(arr)):
                if j == len(arr) - 1:
                    print(arr[j])
                else:
                    print(arr[j], end = ' ')
            break

if __name__ == '__main__':

    arr1 = [1, 3, 5, 9, 13, 22, 27, 35, 46, 51, 55, 83, 87, 23]
    arr2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

    insertionSort1(arr2)