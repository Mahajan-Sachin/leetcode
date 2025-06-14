class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        while i<len(arr):
            if arr[i]==0:
                count+=1
                arr.pop(i)
            else:
                i+=1
        arr.extend([0]*count)
        