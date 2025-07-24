class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        curr=0
        mini=float("inf")
        while(j<len(nums)):
            curr+=nums[j]
            if curr>=target:
                mini=min(mini,j-i+1)
                while curr>=target:
                    curr=curr-nums[i]
                    mini=min(mini,j-i+1)
                    i+=1
            j+=1
        return mini if mini!= float("inf") else 0
            

        