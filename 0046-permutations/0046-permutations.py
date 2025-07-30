class Solution:
    def helper(self,nums,curr,visited,result):
        if len(curr)==len(nums):
            result.append(curr[:])
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            curr.append(nums[i])
            visited[i]=True
            self.helper(nums,curr,visited,result)
            curr.pop()
            visited[i]=False
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        visited=[False]*len(nums)
        self.helper(nums,[],visited,result)
        return result
        