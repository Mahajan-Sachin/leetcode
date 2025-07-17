class Solution:
    def helper(self,nums,curr,result,visited):
        if len(curr)==len(nums):
            result.append(curr[:])
            return
        for i in range(len(nums)):
            if visited[i]==True: #ya old case hi ha, means 46 question wala
                continue
            if i>0 and nums[i]==nums[i-1] and not visited[i-1]:
                continue
            curr.append(nums[i])
            visited[i]=True
            self.helper(nums,curr,result,visited)
            curr.pop()
            visited[i]=False
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        self.helper(nums,[],result,visited=[False]*len(nums))
        return result