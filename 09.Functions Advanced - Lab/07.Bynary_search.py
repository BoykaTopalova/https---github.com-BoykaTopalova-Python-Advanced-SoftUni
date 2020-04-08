def bynary_search(values, target):
    if not values:
        return False
    if len(values) == 1:
        return values[0] == target
    mid = len(values) // 2
    if values[mid] == target:
        return True
    elif values[mid] < target:
        return bynary_search(values[mid:], target)
    else:
        return bynary_search(values[:mid], target)


values = [1, 2, 3, 4, 5, 6, 7, 8, 199, 300]
print(bynary_search(values, 100))
