from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            if freq[num] > 2:
                freq[num] = 2
        final = []
        for key, val in freq.items():
            final.extend([key] * val)   

        for i in range(len(final)):
            nums[i] = final[i]
         
        return len(final)
