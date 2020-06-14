class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        values = []
        current = self

        while current:
            values.append(str(current.value))
            current = current.next
        return '<%s>' % ' -> '.join(values)


class Solution:
    @staticmethod
    def merge_linked_lists(head_one, head_two):

        head = current = LinkedList('H')

        while head_one and head_two:
            if head_one.value < head_two.value:
                current.next = head_one
                head_one = head_one.next
            else:
                current.next = head_two
                head_two = head_two.next
            current = current.next
        else:
            current.next = head_one or head_two

        return head.next

    @staticmethod
    def merge_slls(head_one, head_two):

        prev, p1, p2 = None, head_one, head_two

        while p1 and p2:
            if p1.value < p2.value:
                if prev:
                    prev.next = p1
                prev, p1 = p1, p1.next
            else:
                if prev:
                    prev.next = p2
                prev, p2 = p2, p2.next
        else:
            prev.next = p1 or p2
        return min(head_one, head_two, key=lambda v: v.value)


if __name__ == '__main__':

    s = Solution()
    a, b = LinkedList(1), LinkedList(1)
    x, y = a, b

    for v1, v2 in zip([1, 1, 3, 4, 5, 5, 5, 5, 10], [1, 1, 2, 2, 3, 5, 6, 10, 10]):
        x.next, y.next = LinkedList(v1), LinkedList(v2)
        x, y = x.next, y.next

    print(s.merge_linked_lists(a, b))
