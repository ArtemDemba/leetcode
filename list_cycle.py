"""https://leetcode.com/problems/linked-list-cycle-ii/description/"""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode):
        dct = {}
        pointer = head
        while pointer:
            if pointer.next in dct:
                return pointer.next
            dct[pointer] = pointer.next
            pointer = pointer.next
        return None


s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2.next = node3
node1.next = node2
print(s.detectCycle(node1))
