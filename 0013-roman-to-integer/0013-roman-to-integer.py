class Solution:
    def romanToInt(self, s: str) -> int:
        mp={
            "I":1,"V":5,"IX":9,"X":10,"XX":20,"XL":40,"L":50,"C":100,
            "CD":400,"D":500,"CM":900,"M":1000
        }
        res=0
        for i in range(len(s)):
            if i+1<len(s) and mp[s[i]]<mp[s[i+1]]:
                res-=mp[s[i]]
            else:
                res+=mp[s[i]]
        return res
            
        