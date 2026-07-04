from bisect import bisect_left


def is_ordered(table):
    for i in range(len(table) - 1):
        if table[i][0] > table[i + 1][0]:
            return False

    return True


def binary_search(table, key):
    left = 0
    right = len(table) - 1
    comparisons = 0
    result = -1

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if table[mid][0] == key:
            result = mid
            right = mid - 1
        elif table[mid][0] < key:
            left = mid + 1
        else:
            right = mid - 1

    return result, comparisons


def standard_search(table, key):
    keys = []

    for row in table:
        keys.append(row[0])

    index = bisect_left(keys, key)

    if index < len(keys) and keys[index] == key:
        return index

    return -1
