class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        maxi=float("-inf")
        curr=0
        for i in range(len(arr)):
            curr+=arr[i]
            maxi=max(curr,maxi)
            if curr<0:
                curr=0
        return maxi


    
        