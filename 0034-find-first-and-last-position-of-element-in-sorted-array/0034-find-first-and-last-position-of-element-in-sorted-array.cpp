class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first=-1,end=nums.size()-1,start=0,mid,last=-1;
        while(start<=end){
            mid=end-(end-start)/2;
            if(nums[mid]==target){
                first=mid;
                end=mid-1;
            }
            else if(nums[mid]<target){
                start=mid+1;
            }
            else{
                end=mid-1;
            }

        }
        last=-1,end=nums.size()-1,mid=-1,start=0;
        while(start<=end){
            mid=end-(end-start)/2;
            if(nums[mid]==target){
                last=mid;
                start=mid+1;
            }
            else if(nums[mid]<target){
                start=mid+1;
            }
            else{
                end=mid-1;
            }

        }
        return {first,last};
    }
};