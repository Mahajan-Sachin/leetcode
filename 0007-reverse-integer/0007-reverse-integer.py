class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        Max_int=2**(31)-1
        Min_int=-2**31
        sign=1
        if x<0:
            sign=-1
        x=abs(x)
        while(x!=0):
            last_digit=x%10
            rev=rev*10+last_digit
            x=int(x//10)
        rev=rev*sign
        if rev>Max_int or rev<Min_int:
            return 0
        return rev
        
            

        