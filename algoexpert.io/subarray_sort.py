def subarray_sort(array):

    result = [-1, 1]

    if len(array) > 2:
        unsorted = False
        unsorted_min, unsorted_max = float("inf"), float("-inf")

        for idx, num in enumerate(array):
            if out_of_order(idx, num, array) is True:
                unsorted_min = min(unsorted_min, num)
                unsorted_max = max(unsorted_max, num)
                unsorted = True

        if unsorted is True:
            i = 0
            j = len(array) - 1

            while i < j:
                while i < j and array[i] <= unsorted_min:
                    i += 1
                while i < j and array[j] >= unsorted_max:
                    j -= 1
                result = [i, j]
                break

    return result


def out_of_order(idx, num, array):
    if idx == 0:
        if num > array[idx + 1]:
            return True
    elif idx == len(array) - 1:
        if num < array[idx - 1]:
            return True
    else:
        if array[idx - 1] > num or num > array[idx + 1]:
            return True
    return False


if __name__ == '__main__':

    r = subarray_sort(array=[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
    print(r)

