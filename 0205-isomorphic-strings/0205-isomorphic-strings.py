class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapSt={}
        mapTs={}
        for c1,c2 in zip(s,t):
            if c1 in mapSt and mapSt[c1]!=c2 or c2 in mapTs and mapTs[c2]!=c1:
                return False
            mapSt[c1]=c2
            mapTs[c2]=c1
        return True