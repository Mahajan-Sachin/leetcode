class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        maping={}
        for num in reversed(nums2):
            while stack and stack[-1]<=num:
                stack.pop()
            else:
                maping[num]=stack[-1] if stack else-1
                stack.append(num)
        return [maping[num] for num in nums1]
            