class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            num=nums1[i]
            if num in nums2:
                indx=nums2.index(num)
                greater_found=False
                for j in range(indx+1,len(nums2)):
                    if nums2[j]>num:
                        nums1[i]=nums2[j]
                        greater_found=True
                        break
                if greater_found==False:
                    nums1[i]=-1
            else:
                nums1[i]=-1
        return nums1
