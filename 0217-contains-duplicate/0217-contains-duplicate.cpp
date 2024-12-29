class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int>freq;
        bool flag=false;
        for(int num:nums){
            freq[num]++;
            if(freq[num]>1){
                flag=true;
            }
        }
        return flag;
    }
};