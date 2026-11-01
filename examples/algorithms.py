def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search(sorted_values, target):
    low, high = 0, len(sorted_values) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if sorted_values[middle] == target:
            return middle
        if sorted_values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def count_frequencies(values):
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts
