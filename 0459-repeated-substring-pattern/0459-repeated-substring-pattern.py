class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        total=len(s)
        j=0
        while(j<total-1):
            string=s[:j+1]
            multi=total//len(string)
            if string*multi==s:
                return True
            j+=1
        return False