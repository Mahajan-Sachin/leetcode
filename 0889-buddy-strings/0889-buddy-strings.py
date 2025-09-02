class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        freq_s=Counter(s)
        freq_goal=Counter(goal)
        if freq_s!=freq_goal or len(s)!=len(goal):
            return False
        s=list(s)
        goal=list(goal)
        def checkFreq(s):
            s="".join(s)
            freq=Counter(s)
            for char in s:
                if freq[char]>1:
                    return True
            return False
        if (s==goal):
            return checkFreq(s)
        index=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                index.append(i)
        s[index[0]],s[index[1]]=s[index[1]],s[index[0]]
        return s==goal

