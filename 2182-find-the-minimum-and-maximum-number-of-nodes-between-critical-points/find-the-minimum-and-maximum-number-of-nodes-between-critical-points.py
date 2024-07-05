from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return [-1, -1]
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        critical_points = []
        for i in range(1, len(values) - 1):
            if (values[i] > values[i - 1] and values[i] > values[i + 1]) or (values[i] < values[i - 1] and values[i] < values[i + 1]):
                critical_points.append(i)
        if len(critical_points) < 2:
            return [-1, -1]
        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]
        
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])
        
        return [min_distance, max_distance]
