class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


def shorten_path(path):

    idx = 0
    stack = Stack()

    if path[0] == '/':
        stack.items.append('')

    while idx < len(path):
        while idx < len(path) and path[idx] == '/':
            idx += 1

        temp = []

        while idx < len(path) and path[idx].isalpha():
            temp.append(path[idx])
            idx += 1
        else:
            if temp:
                stack.push(''.join(temp))
                continue

            count = 0

            while idx < len(path) and path[idx] == '.':
                idx += 1
                count += 1

            if count == 2:
                key = '..'
                if stack.is_empty() or stack.peek() == key:
                    stack.push(key)
                elif stack.peek() != '':
                    stack.pop()

    return '/' if stack.peek() == '' else '/'.join(stack.items)


if __name__ == '__main__':

    print(shorten_path("/foo/../test/../test/../foo//bar/./baz"))
