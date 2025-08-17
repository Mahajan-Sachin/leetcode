class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=j=0
        count=0
        vowels="aeiou"
        max_count=-1
        while j<len(s):
            if s[j] in vowels:
                count+=1
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                max_count=max(count,max_count)
                if s[i] in vowels:
                    count-=1
                i+=1
                j+=1
        return max_count

