from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start_time1, end_time1 = map(self.convert_to_int, event1)
        start_time2, end_time2 = map(self.convert_to_int, event2)

        return max(start_time1, start_time2) <= min(end_time1, end_time2)

    def convert_to_int(self, time_str: str) -> int:
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes



## step to solve this problem 
## convert the time to interger 
## then compare the time form event 2 if it lie in between then 
## reurn True
## or else return False
