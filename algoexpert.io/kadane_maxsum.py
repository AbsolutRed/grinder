
def max_sum_subarray(array):

    left, right = 0, len(array) - 1
    left_sum, right_sum = array[0], array[-1]

    while left < right:
        if array[left] < 0 and abs(array[left]) > left_sum:
            left_sum = 0
        else:
            left_sum += array[left]

        if array[right] < 0 and abs(array[right]) > right_sum:
            right_sum = 0
        else:
            right_sum += array[right]

        right -= 1
        left += 1
    else:
        return left_sum + right_sum


def kadanes_algo(array):

    if array:
        current_sum, max_sum = array[0], float("-inf")

        for item in array[1:]:
            current_sum = max(current_sum + item, item)
            max_sum = max(max_sum, current_sum)
        return max_sum


if __name__ == '__main__':

    a = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    print(kadanes_algo(a))
