class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        alphabet_dict = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}  # made a dict for each element
        values_1 = [alphabet_dict[char] for char in s1]  # convert from element to number
        values_2 = [alphabet_dict[char] for char in s2]  # convert from element to number
        values_1.sort()
        values_2.sort()
        can_break_1 = all(v1 >= v2 for v1, v2 in zip(values_1, values_2))
        can_break_2 = all(v2 >= v1 for v1, v2 in zip(values_1, values_2))
        
        return can_break_1 or can_break_2
