class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1=Counter(word1)
        freq2=Counter(word2)
        for char in word1:
            if char not in word2:
                return False
        for char in word2:
            if char not in word1:
                return False
        List1=[v for u,v in freq1.items()]
        List2=[v for u,v in freq2.items()]
        List1.sort()
        List2.sort()
        return List1==List2
            
        
        