# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        # while fast and fast.next인 이유:
        # 리스트의 끝에 도달했을 때 fast.next = None이 된다.
        # int and None = False 이기 때문에 while문에서 나오게 된다.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow