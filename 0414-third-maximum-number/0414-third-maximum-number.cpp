class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> maxSet;
        
        // Insert elements into the set
        for (int num : nums) {
            maxSet.insert(num);
            if (maxSet.size() > 3) {
                // Keep only the top 3 maximums
                maxSet.erase(*maxSet.begin());
            }
        }
        
        // If the set contains 3 elements, return the smallest one
        if (maxSet.size() == 3) {
            return *maxSet.begin();
        }
        
        // Otherwise, return the largest one
        return *maxSet.rbegin();
    }
};