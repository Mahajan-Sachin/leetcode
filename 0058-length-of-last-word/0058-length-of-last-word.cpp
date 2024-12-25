class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0, last = 0;  // Corrected variable declaration
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') {
                length = 0;  // Reset length when space is encountered
            } else {
                length++;    // Increase length for non-space characters
                last = length;  // Store the length of the current word
            }
        }
        return last;  // Return the length of the last word
    }
};
