class Solution:
    def helper(self,arr,index,curr,result):
        if index>=len(arr):
            result.append(curr[:])
            return
        #exclude
        self.helper(arr,index+1,curr,result)
        #include:
        curr.append(arr[index])
        self.helper(arr,index+1,curr,result)
        curr.pop()
    def subsets(self, arr: List[int]) -> List[List[int]]:
        result=[]
        self.helper(arr,0,[],result)
        return result
        