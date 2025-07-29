class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq={}
        matrix_sum=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                freq[grid[i][j]]=freq.get(grid[i][j],0)+1
                matrix_sum+=grid[i][j]
        n=len(grid)
        limit=n**2
        sumi=limit*(limit+1)//2
        duplicate=-1
        for num in freq:
            if freq[num]==2:
                duplicate=num
        missing_val=sumi-(matrix_sum-duplicate)
        return [duplicate,missing_val]
        
        