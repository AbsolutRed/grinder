#!/usr/bin/env python3


def find_common(d):

    common = set()

    if d:
        user = next(iter(d))
        common = set(d[user])

        for books in d.values():
            common = common.intersection(books)

    return common


if __name__ == '__main__':

    user_books = {
        'user1': ['book1', 'book2', 'book3', 'book4'],
        'user2': ['book1', 'book2'],
        'user3': ['book2', 'book3'],
    }

    result = find_common(user_books)
    assert result == {'book2'}

    user_books = {
        'user1': ['book1', 'book2', 'book3', 'book4'],
        'user2': ['book1', 'book2'],
        'user3': ['book3', 'book4'],
    }

    result = find_common(user_books)
    assert result == set()
