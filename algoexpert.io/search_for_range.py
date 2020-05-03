
def search_for_range(array, target):

    total_nums = len(array)
    target_idx = binary_search(array, 0, total_nums - 1, target)
    return target_idx


def binary_search(array, start, end, target):

    if start > end:
        return -1

    middle = (start + end) // 2

    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return binary_search(array, start, middle - 1, target)
    else:
        return binary_search(array, middle + 1, end, target)


if __name__ == '__main__':

    a = [4, 5, 8, 9, 13]

    for num in range(10):
        print(search_for_range(a, num))
