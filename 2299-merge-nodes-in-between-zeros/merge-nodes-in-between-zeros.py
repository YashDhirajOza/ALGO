class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        head = head.next
        sum_val = 0
        while head:
            if head.val == 0:
                cur.next = ListNode(sum_val)
                cur = cur.next
                sum_val = 0
            sum_val += head.val
            head = head.next
        return dummy.next