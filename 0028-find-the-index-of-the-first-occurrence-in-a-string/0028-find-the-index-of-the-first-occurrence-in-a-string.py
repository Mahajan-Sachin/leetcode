class Solution:
    def strStr(self, text: str, patt: str) -> int:
        len1=len(text)
        len2=len(patt)
        i=0
        j=0
        while j<len(text):
            if j-i+1<len2:
                j+=1
            if j-i+1==len2:
                if text[i:j+1]==patt:
                    return i
                i+=1
                j+=1
        return -1

         
            
        