

def largest_range_no_sort(array):
    """
    Time O(n) | Space O(n)
    """
    largest = None
    data = {x: True for x in array}

    for d in array:
        if data[d] is False:
            continue

        low = high = d
        data[d] = False

        while low - 1 in data:
            low -= 1
            data[low] = False

        while high + 1 in data:
            high += 1
            data[high] = False

        if not largest or largest[1] - largest[0] < high - low:
            largest = [low, high]
    return largest


def largest_range(array):
    """
    Time -> O(NLogN) | Space -> O(1)
    """
    bound = len(array)

    if bound == 1:
        return [array[0], ] * 2

    idx = 1
    array = sorted(array)
    largest, temp_range = None, None

    while idx < bound:
        clear = False
        if array[idx] - 1 == array[idx - 1]:
            if not temp_range:
                temp_range = [array[idx - 1], array[idx]]
            else:
                temp_range[1] = array[idx]

            if (largest is None and temp_range) or all(
                    (largest, temp_range, temp_range[1] - temp_range[0] > largest[1] - largest[0])):
                largest = temp_range
        elif array[idx] != array[idx - 1] and array[idx] - 1 != array[idx - 1]:
            clear = True
        idx += 1

        if clear is True and temp_range:
            temp_range = None
    return largest


if __name__ == '__main__':

    a = [8, 4, 2, 10, 3, 6, 7, 9, 1]
    b = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    c = [19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]

    for i in (a, b, c):
        print(largest_range_no_sort(i))
