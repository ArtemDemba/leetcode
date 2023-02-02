"""https://leetcode.com/problems/middle-of-the-linked-list/?envType=study-plan&id=level-1"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        middle = count // 2
        result = head
        for _ in range(middle):
            result = result.next
        return result


s = Solution()
node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(s.middleNode(node1))
