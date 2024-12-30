class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum_arr=0;
        int n=nums.size();
        for(int i=0;i<nums.size();i++) sum_arr=nums[i]+sum_arr;
        int actual=n*(n+1)/2;
        return actual-sum_arr;
    }
};