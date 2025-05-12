class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currSum=0,maxi=INT_MIN;
        for(int i=0;i<nums.size();i++){
            currSum=currSum+nums[i];
            maxi=max(currSum,maxi);
            if(currSum<0){
                currSum=0;
            }
        }
        return maxi;
    }
};