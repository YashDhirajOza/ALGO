class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        for i in range(0, len(nodes), k):
            if i + k <= len(nodes):
                nodes[i:i+k] = reversed(nodes[i:i+k])
        dummy = ListNode(0)  # Dummy head
        current = dummy
        for node in nodes:
            current.next = node
            current = current.next
        current.next = None  
        return dummy.next
