# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, curr = None, ListNode(0, head)
        start = end = None
        after_start = before_end = None
        cnt = 0
        flag = False
        while curr:
            if cnt == left - 1:
                start = curr
                flag = True
            if cnt == right + 1:
                end = curr
                flag = False
            if cnt == left:
                after_start = curr
            if cnt == right:
                before_end = curr
            if flag:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            else:
                curr = curr.next
            cnt += 1

        after_start.next = end
        start.next = before_end
        
        if left == 1:
            return before_end
        else:
            return head