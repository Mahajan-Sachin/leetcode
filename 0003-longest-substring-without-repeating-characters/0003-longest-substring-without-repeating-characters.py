class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set=set()
        left=right=0
        if len(s)==0:
            return 0
        length=-1
        while right<len(s)-1:
            while Set and s[right] in Set:
                Set.remove(s[left])
                left+=1
            Set.add(s[right])
            length=max(length,right-left+1)
            right+=1
        return length
        