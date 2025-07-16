class Solution:
    def helper(self,nums,curr,result):
        if len(curr)==len(nums):
            result.append(curr[:])
            return
        for num in nums:
            if num in curr:
                continue
            curr.append(num)
            self.helper(nums,curr,result)
            curr.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.helper(nums,[],result)
        return result
        