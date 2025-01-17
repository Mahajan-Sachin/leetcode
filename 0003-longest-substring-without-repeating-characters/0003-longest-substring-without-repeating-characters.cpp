class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> window; // To store unique characters in the current window
        int i = 0, j = 0; // Sliding window pointers
        int maxi = 0; // Maximum length of substring without repeating characters

        while (j < s.size()) {
            // If the character is not in the window, expand the window
            if (window.find(s[j]) == window.end()) {
                window.insert(s[j]);
                maxi = max(maxi, j - i + 1); // Update the maximum length
                j++;
            } 
            // If the character is already in the window, shrink the window from the left
            else {
                window.erase(s[i]);
                i++;
            }
        }

        return maxi;
    }
};
