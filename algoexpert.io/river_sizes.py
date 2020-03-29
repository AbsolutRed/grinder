"""
You are given a 2-D array (matrix) of potentially unequal height and width containing only 0s and 1s.
Each 0 represents 'land' and each 1 represents part of a river. A river consists of any number of 1s that are either
horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine
its size. Write a function that returns an array of the sizes of all rivers represented in the input matrix.

NOTE: These sizes do not need to be in any particular order.

Sample input:
[
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]

Sample output >> [1, 2, 2, 2, 5]
"""


class Solution:
    def __init__(self):
        pass


if __name__ == '__main__':

    data = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]

