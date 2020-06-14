def _longest_palindromic_substr(string):
    """T: O(n^3) | S: O(1)"""
    def is_palindrome(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    if len(string) < 2:
        return string

    longest_substr = (0, 1)

    for i in range(len(string)):
        for j in range(i, len(string)):
            if is_palindrome(string, i, j):
                longest_substr = max(
                    longest_substr, (i, j + 1), key=lambda x: x[1] - x[0])
    return string[longest_substr[0]:longest_substr[1]]


def longest_palindromic_substring(string):
    """T: O(n^2) | S: O(1)"""
    if len(string) < 2:
        return string

    longest = (0, 1)

    for idx in range(1, len(string)):
        odd = _find_longest(string, idx - 1, idx + 1)
        even = _find_longest(string, idx - 1, idx)

        longest = max(longest, even, odd, key=lambda x: x[1] - x[0])
    return string[longest[0]:longest[1]]


def _find_longest(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        right += 1
        left -= 1
    return left + 1, right


if __name__ == '__main__':

    data = 'abaxyzzyxf'
    print(longest_palindromic_substring(data))
