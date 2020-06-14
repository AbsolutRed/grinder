#!/usr/bin/env python3
"""
flatten(1, [2, 3], 4, 5, [6, [7]]) -> [1, 2, 3, 4, 5, 6, 7]

flatten('a', ['b', 2], 3, None, [[4], ['c']]) -> ['a', 'b', 2, 3, None, 4, 'c']

flatten(['1', 9], ('x', 0, [2]), [[4], 'z'], {'k': [11, [9, 'x']]}
"""


def flatten(*args):

    result = []

    for x in args:
        if isinstance(x, (list, tuple, set)):
            result.extend(flatten(*x))
        elif isinstance(x, dict):
            result.extend(flatten(*[(k, v) for k, v in x.items()]))
        else:
            result.append(x)
    return result


if __name__ == '__main__':

    r = flatten(['1', 9], ('x', 0, [2]), [[4], 'z'], {'k': [11, [9, 'x']]})
    print(r)
