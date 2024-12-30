class Solution {
public:
    void moveZeroes(vector<int>& nums) {
         int left = 0; // Pointer to place the next non-zero element

    // Traverse the array with right pointer
    for (int right = 0; right < nums.size(); ++right) {
        if (nums[right] != 0) {
            // Swap non-zero element to the left pointer's position
            std::swap(nums[left], nums[right]);
            left++;
        }
    }
    }
};