"""
Write a function that takes in an integer n and returns the nth Fibonacci number.

The Fibonacci sequence is defined as follows:
> the first number of the sequence is 0, the second number is 1 and
  the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
"""


def recursive_fibonacci(n):
    """
    Recursive approach -> Time: O(2^n) | Space: O(n)
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def memoized_fibonacci(n):
    """
    Memoized approach -> Time: O(n) | Space: O(n)
    """
    memoize = {}
    
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        if n not in memoize.keys():
            memoize[n] = memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
        return memoize[n]


def iterative_fibonacci(n):
    """
    Iterative approach: Time: O(n) | Space: O(1)
    """
    result = [0, 1]
    n = 1 if n <= 0 else n

    while n > 2:
        result[0], result[1] = result[1], result[0] + result[1]
        n -= 1
    return result[n - 1]


if __name__ == '__main__':

    r = iterative_fibonacci(5)
    print(r)
