class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid=len(s)//2
        vowels=["a","e","i","o","u"]
        count1=count2=0
        i=0
        while (mid<len(s)):
            if s[mid].lower() in vowels:
                count2+=1
            if s[i].lower() in vowels:
                count1+=1
            i+=1
            mid+=1
        return count1==count2
            

