class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            temp_max=max(nums[i],curr_max*nums[i],curr_min*nums[i])
            temp_min=min(nums[i],curr_max*nums[i],curr_min*nums[i])
            curr_max=temp_max
            curr_min=temp_min
            result=max(result,curr_max)
        return result      