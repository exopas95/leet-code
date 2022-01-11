# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(-1)
        temp.next = head
        front = back = temp
        
        for i in range(n):
            front = front.next
        
        while front and front.next:
            back = back.next
            front = front.next
        
        back.next = back.next.next
        return temp.next