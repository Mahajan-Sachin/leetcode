class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        track={}
        track[0]=1
        cum_sum=0
        result=0
        for i in range(len(nums)):
            cum_sum+=nums[i]
            if cum_sum-k in track:
                result+=track[cum_sum-k]
            track[cum_sum]=track.get(cum_sum,0)+1
        return result
        