class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0 
        for i in range(len(details)):
            age_str = details[i][11:13]  
            age = int(age_str)  
            if age > 60:
                counter += 1
        return counter