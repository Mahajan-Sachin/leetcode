class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:  # cleaner empty string check
            return ""
        
        vowels = "aeiouAEIOU"
        s = list(s)
        i, j = 0, len(s) - 1
        
        while i < j:  # strictly less than
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        return "".join(s)
