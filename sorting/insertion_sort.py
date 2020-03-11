def insertion_sort(unsorted):

    for i in range(len(unsorted)):
        x = 1
        temp = unsorted[i]
        while i - x >= 0 and temp < unsorted[i - x]:
            unsorted[i - x + 1] = unsorted[i - x]
            unsorted[i - x] = temp
            x = x + 1
    return unsorted

print(insertion_sort([]))
print(insertion_sort([6]))
print(insertion_sort([8, 5]))
print(insertion_sort([8, 7, 5]))
print(insertion_sort([8, 7, 5, 4]))
print(insertion_sort([3, 8, 7, 5, 4]))
print(insertion_sort([8, 7, 5, 4, 3]))