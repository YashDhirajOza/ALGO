class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst)
                lst = lst.next
        nodes.sort(key=lambda x: x.val)
        head = ListNode(0)  # Dummy head
        current = head
        for node in nodes:
            current.next = node
            current = current.next
        current.next = None  
        return head.next
