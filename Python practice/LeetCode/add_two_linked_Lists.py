# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        h1 = l1
        h2 = l2
        ans = ListNode(0)
        ansPtr = ans
        while h1 or h2 or carry:
            val = carry
            if h1:
                val += h1.val
                h1 = h1.next
            if h2:
                val += h2.val
                h2 = h2.next
            carry = val // 10
            val = val % 10
            ansPtr.next = ListNode(val)
            ansPtr = ansPtr.next
        return ans.next

n1 = ListNode(2, ListNode(4, ListNode(3)))
n2 = ListNode(5, ListNode(6, ListNode(4)))

s = Solution()
print(s.addTwoNumbers(n1, n2).val)
# print(s.addTwoNumbers(n1, n2).next.val)