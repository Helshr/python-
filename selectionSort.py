def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(1, len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))
        print(newArr)
    return newArr


print(selectionSort([2, 1, 5, 6, 100, 7]))