# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for _ in range(left -1):
            prev = prev.next
        cur = prev.next
        for _ in range(right - left):
            temp = prev.next
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = temp
        return dummy.next
# Time complexity: O(n)
# Space complexity: O(1)
