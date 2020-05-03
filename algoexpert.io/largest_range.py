

def largest_range_sorted(array):

    bound = len(array)

    if bound == 0:
        return []
    elif bound == 1:
        return [array[0], array[0]]
    else:
        idx = 1
        array.sort()
        max_range = None

        while idx < bound:
            check = False
            temp_range = [None, None]

            while idx < bound and (array[idx] == array[idx - 1] + 1 or array[idx] == array[idx - 1]):
                if temp_range[0] is None:
                    temp_range[0] = idx - 1
                    check = True
                idx += 1
            else:
                if check is True:
                    temp_range[1] = idx - 1
                    if max_range is None or temp_range[1] - temp_range[0] > max_range[1] - max_range[0]:
                        max_range = temp_range
                idx += 1

        return [array[max_range[0]], array[max_range[1]]] if max_range else []


def largest_range(array):
    """
    Time O(n) | Space O(n)
    """
    max_range = None
    data = {x: False for x in array}

    for d in array:
        if data[d] is True:
            continue

        low = high = d
        data[d] = True

        while low - 1 in data:
            low -= 1
            data[low] = False

        while high + 1 in data:
            high += 1
            data[high] = False

        if max_range is None or max_range[1] - max_range[0] < high - low:
            max_range = [low, high]

    return max_range


if __name__ == '__main__':

    a = [8, 4, 2, 10, 3, 6, 7, 9, 1]
    b = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    c = [19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]

    for i in (a, b, c):
        print(largest_range(i))
