class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s=="":
            return 0
        open=0
        insertion=0
        for char in s:
            if char=="(":
                open+=1
            else: # ")"
                if open>0:
                    open-=1
                else:
                    insertion+=1
        return open+insertion
        