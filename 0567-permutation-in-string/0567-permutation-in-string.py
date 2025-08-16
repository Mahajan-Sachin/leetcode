class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        if k<len(s1):
            return False
        i=j=0
        freq_s1=Counter(s1)
        freq={}
        while j<len(s2):
            freq[s2[j]]=freq.get(s2[j],0)+1
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                if freq_s1==freq:
                    return True
                else:
                    freq[s2[i]]-=1
                    if freq[s2[i]]==0:
                        del freq[s2[i]]
                    i+=1
                    j+=1
        return False

        