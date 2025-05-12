class Solution {
public:
    vector<int> twoSum(vector<int>& arr, int target) {
        unordered_map<int,int>map;
        for(int i=0;i<arr.size();i++){
            int val=target-arr[i];
            if(map.find(val)!=map.end()){
                return {map[val]+1,i+1};
            }
            else{
                map[arr[i]]=i;
            }
        }
        return {};
    }
};