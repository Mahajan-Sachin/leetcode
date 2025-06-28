class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        i=0
        j=0
        maxi=float("-inf")
        window_sum=0
        while j<len(arr):
            window_sum+=arr[j]
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                maxi=max(maxi,window_sum)
                window_sum-=arr[i]
                i+=1
                j+=1
        return maxi/k

        