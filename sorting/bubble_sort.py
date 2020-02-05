def bubble_sort(unsorted):
    
    for i in range(len(unsorted) - 1):
        x = 0
        while x < (len(unsorted) - 1 - i):
            if (unsorted[x + 1] < unsorted[x]):
                temp = unsorted[x + 1]
                unsorted[x + 1] = unsorted[x]
                unsorted[x] = temp 
            x = x + 1
    
    return unsorted

print(bubble_sort([]))
print(bubble_sort([6]))
print(bubble_sort([6, 5]))
print(bubble_sort([6, 5, 4]))
print(bubble_sort([6, 5, 4, 3]))
print(bubble_sort(['s', 'h', 'n', 'r']))