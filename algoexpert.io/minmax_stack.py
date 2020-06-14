class MinMaxStackSimple:

    def __init__(self):
        self.stack = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1][0]

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()[0]

    def push(self, number):
        if len(self.stack) > 0:
            top = self.stack[-1]
            current_min, current_max = top[1], top[2]
            current_max = max(number, current_max)
            current_min = min(number, current_min)
            self.stack.append((number, current_min, current_max))
        else:
            self.stack.append((number,) * 3)

    @property
    def min(self):
        if len(self.stack) > 0:
            return self.stack[-1][1]

    @property
    def max(self):
        if len(self.stack) > 0:
            return self.stack[-1][-1]


class MinMaxStack:
    class CacheElement:
        def __init__(self, value, count):
            self.value = value
            self.count = count

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def update_min(self, element):
        current_min = self.getMin()

        if current_min is None or current_min > element.value:
            self.min_stack.append(element)
        elif current_min == element.value:
            self.min_stack[-1].count += 1

    def update_max(self, element):
        current_max = self.getMax()

        if current_max is None or current_max < element.value:
            self.max_stack.append(element)
        elif current_max == element.value:
            self.max_stack[-1].count += 1

    def peek(self):
        if self.is_empty() is False:
            return self.stack[-1]

    def pop(self):
        if self.is_empty() is False:
            current_min, current_max = self.getMin(), self.getMax()
            num = self.stack.pop()

            if num == current_min:
                self.min_stack[-1].count -= 1
                if self.min_stack[-1].count == 0:
                    self.min_stack.pop()

            if num == current_max:
                self.max_stack[-1].count -= 1
                if self.max_stack[-1].count == 0:
                    self.max_stack.pop()
            return num

    def push(self, number):

        element = self.CacheElement(number, 1)
        self.update_min(element)
        self.update_max(element)
        self.stack.append(number)

    @property
    def min(self):
        if self.is_empty() is False:
            return self.min_stack[-1].value

    @property
    def max(self):
        if self.is_empty() is False:
            return self.max_stack[-1].value
