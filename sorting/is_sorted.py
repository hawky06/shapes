def is_sorted(sorted):
    x = 0
    while x < len(sorted) - 1:
        if (sorted[x] > sorted[x + 1]):
            return False
        x = x + 1
    return True


# Tests
print(is_sorted([5, 6]))
print(is_sorted([6, 5]))
print(is_sorted([]))
print(is_sorted([5]))
print(is_sorted([3, 5, 4]))
print(is_sorted([3, 4, 5, 6]))  # True
print(is_sorted([5, 6, 4, 3]))  # False
print(is_sorted([4, 4]))