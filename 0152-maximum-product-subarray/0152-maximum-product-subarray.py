class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr=nums[0]
        curr_min=nums[0]
        curr_maxi=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            temp_min=min(nums[i],curr_min*nums[i],curr_maxi*nums[i])
            temp_max=max(nums[i],curr_min*nums[i],curr_maxi*nums[i])
            curr_min=temp_min
            curr_maxi=temp_max
            result=max(curr_maxi,result)
        return result
