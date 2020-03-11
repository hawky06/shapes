def merge_lists(list1, list2):
    merged = []
    x1 = 0
    x2 = 0

    for i in range(len(list1) + len(list2)):
        if x1 == len(list1):
            merged.append(list2[x2])
            x2 = x2 + 1
        elif x2 == len(list2):
            merged.append(list1[x1])
            x1 = x1 + 1
        elif list1[x1] < list2[x2]:
            merged.append(list1[x1])
            x1 = x1 + 1
        else:
            merged.append(list2[x2])
            x2 = x2 + 1
    return merged

print(merge_lists([1, 3, 4], [2]))
print(merge_lists([1], [2, 3, 4]))
print(merge_lists([5], [2]))
print(merge_lists([], []))
print(merge_lists([1, 3], [2, 3, 5]))