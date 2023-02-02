"""https://leetcode.com/problems/reverse-linked-list/description/"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prev = None
        current = head

        while current:
            pointer = current.next
            current.next = prev
            prev = current
            current = pointer

        return prev


s = Solution()
third = ListNode(3)
second = ListNode(2, third)
first = ListNode(1, second)

print(s.reverseList(first))