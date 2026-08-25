# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        curr = head
        start = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        prev = None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid=nxt
        
        first = head
        mid = prev
        
        while mid:
            temp1,temp2 = first.next,mid.next
            first.next=mid
            mid.next=temp1
            first = temp1
            mid = temp2

        