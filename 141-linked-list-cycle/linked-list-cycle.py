class Solution:
    def hasCycleHelper(self, node: ListNode, visited: set) -> bool:
        if not node:
            return False
        if node in visited:
            return True
        visited.add(node)
        return self.hasCycleHelper(node.next, visited)
    
    def hasCycle(self, head: ListNode) -> bool:
        return self.hasCycleHelper(head, set())