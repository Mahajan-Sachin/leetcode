#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end()); // Sort the array
        
        long long total = 0; // Tracks the total operations needed for the current window
        int left = 0;        // Left pointer of the sliding window
        int result = 0;      // Stores the maximum frequency
        
        for (int right = 0; right < nums.size(); right++) {
            // Add nums[right] to the total for calculating operations
            total += nums[right];
            
            // If the operations required exceed k, shrink the window
            while ((long long)(nums[right]) * (right - left + 1) - total > k) {
                total -= nums[left];
                left++;
            }
            
            // Update the maximum frequency
            result = max(result, right - left + 1);
        }
        
        return result;
    }
};
