class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        length=len(s)//2
        count1=count2=0
        vowels=["a","e","i","o","u"]
        first=s[:length]
        second=s[length:]
        for char in first:
            if char in vowels:
                count1+=1
        for char in second:
            if char in vowels:
                count2+=1
        return count1==count2
        

