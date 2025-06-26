class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        nums[:]=[0]*freq.get(0,0)+[1]*freq.get(1,0)+[2]*freq.get(2,0) #always use [:] iska bina original replace nehi hota
        