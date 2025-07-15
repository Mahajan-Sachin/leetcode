class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[]
        def left(nums,target,result):
            start=0
            end=len(nums)-1
            val_left=-1
            while start<=end:
                mid=int(start+(end-start)/2)
                if nums[mid]==target:
                    val_left=mid
                    end=mid-1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            result.append(val_left)

        def right(nums,target,result):
            start=0
            end=len(nums)-1
            val_right=-1
            while start<=end:
                mid=int(start+(end-start)/2)
                if nums[mid]==target:
                    val_right=mid
                    start=mid+1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            result.append(val_right)
        left(nums,target,result)
        right(nums,target,result)
        return result
        