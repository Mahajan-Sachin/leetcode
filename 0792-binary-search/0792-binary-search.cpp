class Solution {
public:
    int search(vector<int>& nums, int target) {
        int length=nums.size(),start=0,end=length-1,mid;
        while(start<=end){
            mid=start+(end-start)/2;
            if(nums[mid]==target){
                return mid;
            }
            else if(nums[mid]>target){
                end=mid-1;
            }
            else{
                start=mid+1;
            }
        }
        return -1;
    }
};