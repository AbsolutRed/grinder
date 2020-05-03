
def find_longest_peak(array):

    longest_peak = 0
    bound = len(array)

    if bound > 2:

        i, j, k = 0, 1, 2

        while k < bound:
            if array[i] < array[j] and array[j] > array[k]:
                while k + 1 < bound and array[k + 1] < array[k]:
                    k += 1
                longest_peak = max(longest_peak, (k - i) + 1)
                i, j, k = k, k + 1, k + 2
            elif array[k] == array[j] or array[i] > array[j]:
                while k + 1 < bound and array[k + 1] == array[k]:
                    k += 1
                i, j, k = k, k + 1, k + 2
            elif array[i] == array[j]:
                i, j, k = j, k, k + 1
            else:
                j += 1
                k += 1

    return longest_peak


if __name__ == '__main__':

    data = [
        [1, 3, 2],
        [1, 1, 3, 2, 1],
        [1, 2, 3, 4, 5, 1],
        [5, 4, 3, 2, 1, 2, 1],
        [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3],
    ]

    for item in data:
        peak = find_longest_peak(item)
        print(peak)
