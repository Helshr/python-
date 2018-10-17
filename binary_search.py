# 接受一个有序数组和一个元素
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + high
        guess = list[mid]
        if item == guess:
            return mid
        elif item < guess:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5]


print(binary_search(my_list, 3))
print(binary_search(my_list, -1))