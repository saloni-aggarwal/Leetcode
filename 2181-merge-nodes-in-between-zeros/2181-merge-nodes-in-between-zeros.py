# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = temp = ListNode()
        s = 0
        head = head.next
        while head:
            s += head.val
            if head.val == 0:
                temp.next = ListNode(s)
                temp = temp.next
                s = 0
            head = head.next
        # print("temp =", temp)
        # print("res =", res)
        return res.next
        