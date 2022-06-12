from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Val = l1.val
        i = 1

        while l1.next != None:
            l1 = l1.next
            l1Val += l1.val * (10 ** i)
            i += 1

        l2Val = l2.val
        i = 1

        while l2.next != None:
            l2 = l2.next
            l2Val += l2.val * (10 ** i)
            i += 1

        finalVal = l1Val + l2Val
        finalNode = ListNode()
        toReturn = ListNode()
        i = 1

        while finalVal != 0:
            finalNode.next = ListNode(finalVal % 10)
            finalVal = finalVal // 10
            if i == 1: toReturn = finalNode.next # don't lose the head
            finalNode = finalNode.next
            i += 1

        return toReturn


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

p1 = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
fin = p1.addTwoNumbers(l1, l2)

print(fin)