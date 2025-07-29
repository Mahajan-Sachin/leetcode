class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        freq=Counter(nums)
        sorting=sorted(freq.items(),key=lambda x: x[1],reverse=True)
        List=[key for key,value in sorting]
        return List[0]
        