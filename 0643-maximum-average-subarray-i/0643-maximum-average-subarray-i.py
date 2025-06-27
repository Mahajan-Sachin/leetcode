class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        maxi_sum=window_sum
        for i in range(k,len(nums)):
            window_sum=nums[i]+window_sum-nums[i-k]
            maxi_sum=max(maxi_sum,window_sum)
        return  maxi_sum/k    