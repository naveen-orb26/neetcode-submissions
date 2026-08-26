"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
                on={None:None}
                curr=head
                while curr:
                    on[curr]=Node(curr.val)
                    curr=curr.next
                curr=head
                while curr:
                    copy = on[curr]
                    copy.next=on[curr.next]
                    copy.random = on[curr.random]
                    curr=curr.next
                return on[head]