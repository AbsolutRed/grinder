#!/usr/bin/env python3
"""
Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a^b.
Note that a and b may be very large! For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969.
The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6. Also, please take 0^0 to be 1.

You may assume that the input will always be valid.
"""


def last_digit(x, y):

    while x >= 10:
        x = x % 10

    if y == 0:
        return 1
    elif x == 0 or y == 1:
        return x
    else:
        y = y % 4
        power = 4 if y == 0 else y
        return int(str(x ** power)[-1])


if __name__ == '__main__':

    assert last_digit(4, 1) == 4
    assert last_digit(4, 2) == 6
    assert last_digit(9, 7) == 9
    assert last_digit(10, 10 ** 10) == 0
    assert last_digit(2 ** 200, 2 ** 300) == 6
    assert last_digit(11135114806789805803664796608728130249421015590859009747752,
                      9004828295231684203192440003075209156209765648738929150312) == 6
