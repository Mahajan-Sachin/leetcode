class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        freq=Counter(nums)
        for num in freq:
            if freq[num]==1:
                return num
        