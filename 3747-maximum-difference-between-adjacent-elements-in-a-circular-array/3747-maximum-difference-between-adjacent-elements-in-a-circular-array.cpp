class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int max_diff = 0;
    
    // Iterate through the array to find differences between adjacent elements
    for (int i = 0; i < nums.size(); ++i) {
        // Calculate the next index in a circular manner
        int next_index = (i + 1) % nums.size();
        
        // Calculate the absolute difference and update max_diff if necessary
        max_diff = max(max_diff, abs(nums[i] - nums[next_index]));
    }
    
    return max_diff;
    }
};