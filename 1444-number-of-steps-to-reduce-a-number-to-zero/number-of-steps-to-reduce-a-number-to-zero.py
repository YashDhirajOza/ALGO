class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter=0
        n=num
        while n!=0:
            if n%2==0:
                n=n/2
                counter= counter +1 
            else:
                n=n-1
                counter = counter +1 
        return counter 
            
        
        