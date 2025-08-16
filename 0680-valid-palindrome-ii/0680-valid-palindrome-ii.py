class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        def valid(s,left,right):
            while left<right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            elif s[left]!=s[right]:
                return valid(s,left+1,right) or valid(s,left,right-1)
        return True