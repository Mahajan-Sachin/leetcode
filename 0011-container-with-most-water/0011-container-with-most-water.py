class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        area=float("-inf")
        while(left<right):
            eff_ht=min(height[left],height[right])
            eff_wd=right-left
            area=max(area,eff_ht*eff_wd)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area
        