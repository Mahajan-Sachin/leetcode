class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for char in strs:
            key="".join(sorted(char))
            result[key].append(char)
        return list(result.values())
        
        