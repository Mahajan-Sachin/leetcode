class Solution:
    def firstUniqChar(self, s: str) -> int:
        for char in s:
            if s.index(char)==s.rindex(char):
                return s.index(char)
        return -1
        
        