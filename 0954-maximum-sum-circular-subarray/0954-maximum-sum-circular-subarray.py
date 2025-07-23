class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def NormalKadane(arr):
            curr=arr[0]
            maxi=arr[0]
            for i in range(1,len(arr)):
                curr=max(arr[i],arr[i]+curr)
                maxi=max(curr,maxi)
            return maxi 
        def min_subarray(arr):
            curr=arr[0]
            mini=arr[0]
            for i in range(1,len(arr)):
                curr=min(arr[i],arr[i]+curr)
                mini=min(curr,mini)
            return mini 
        def Total_sum(arr):
            return sum(arr)
        Max_Sum=NormalKadane(nums)
        Circular_Sum=Total_sum(nums)-min_subarray(nums)
        if Max_Sum>0:
            return max(Max_Sum,Circular_Sum)
        else:
            return Max_Sum
         
        