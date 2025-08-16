class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=list(word1)
        word2=list(word2)
        word3=[]
        Range=min(len(word1),len(word2))
        for i in range(Range):
            word3.append(word1.pop(0)+word2.pop(0))
        while word1:
            word3.append(word1.pop(0))
        while word2:
            word3.append(word2.pop(0))
        return "".join(word3)

        