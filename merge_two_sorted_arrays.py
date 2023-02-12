"""https://leetcode.com/problems/merge-sorted-array/?envType=study-plan&id=data-structure-i"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = current = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next

        if list1 or list2:
            current.next = list1 if list1 else list2
        return result.next


if __name__ == '__main__':
    s = Solution()
    list1 = ListNode(-9, ListNode(3))
    list2 = ListNode(5, ListNode(7, ListNode(10, ListNode(14))))

    res = s.mergeTwoLists(list1, list2)
    while res:
        print(res.val, end=', ')
        res = res.next
    # print(res.val)

