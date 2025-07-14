class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=[]
        for char in s:
            if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" or char=="A" or char=="E" or char=="I" or char=="O" or char=="U":
                vowels.append(char)
        vowels.sort()
        s=list(s)
        for i in range(len(s)):
            if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u" or s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U":
                if vowels:
                    s[i]=vowels[0]
                    vowels.pop(0)
        return "".join(s)

            
        