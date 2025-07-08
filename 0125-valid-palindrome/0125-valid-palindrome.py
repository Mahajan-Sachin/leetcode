class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().strip()
        result=""
        for char in s:
            if char.isalnum():
                result+=char
        start=0
        end=len(result)-1
        while start<=end:
            if result[start]!=result[end]:
                return False
            start+=1
            end-=1
        return True

                
        