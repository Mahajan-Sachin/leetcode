class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";

        int n = s.size();
        int start = 0, maxLength = 0;

        // Function to expand around the center
        auto expandAroundCenter = [&](int left, int right) {
            while (left >= 0 && right < n && s[left] == s[right]) {
                left--;
                right++;
            }
            return right - left - 1; // Length of the palindrome
        };

        for (int i = 0; i < n; i++) {
            // Odd-length palindrome
            int len1 = expandAroundCenter(i, i);
            // Even-length palindrome
            int len2 = expandAroundCenter(i, i + 1);

            // Maximum length for the current center
            int len = max(len1, len2);

            // Update the start and maxLength if a longer palindrome is found
            if (len > maxLength) {
                maxLength = len;
                start = i - (len - 1) / 2; // Calculate starting index
            }
        }

        return s.substr(start, maxLength);
    }
};
