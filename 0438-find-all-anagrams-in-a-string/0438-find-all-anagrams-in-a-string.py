class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        freq_p=Counter(p)
        freq={}
        i=j=0
        result=[]
        while j<len(s):
            freq[s[j]]=freq.get(s[j],0)+1
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                if freq_p==freq:
                    result.append(i)
                freq[s[i]]-=1
                if freq[s[i]]==0:
                    del freq[s[i]]
                i+=1
                j+=1
        return result
        