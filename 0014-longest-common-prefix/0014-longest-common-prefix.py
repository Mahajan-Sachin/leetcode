class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        result=""
        last=strs[len(strs)-1]
        Range=min(len(first),len(last))
        for i in range(Range):
            if last[i]==first[i]:
                result+=last[i]
            else:
                break
        return result
            

        