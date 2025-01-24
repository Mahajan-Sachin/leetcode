class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
          sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int i = 0; // Pointer for greed factors
        int j = 0; // Pointer for cookie sizes
        int count = 0; // Count of content children
        
        // Step 2: Use two pointers to match cookies to children
        while (i < g.size() && j < s.size()) {
            if (s[j] >= g[i]) { 
                // If the cookie satisfies the child's greed factor
                count++;
                i++; // Move to the next child
                j++; // Move to the next cookie
            } else {
                // Otherwise, move to the next larger cookie
                j++;
            }
        }
        
        return count;
    }
};