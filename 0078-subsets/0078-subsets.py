class Solution:
    def solve(self,nums,index,result,output):
        if (index>=len(nums)):
            result.append(output[:])
            return
        #exclude:
        self.solve(nums,index+1,result,output)
        #include
        output.append(nums[index])
        self.solve(nums,index+1,result,output)
        output.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[] # ultimate reult
        self.solve(nums,0,result,[])
        return result

        
        
        
        