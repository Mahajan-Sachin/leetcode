class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        
        // Step 1: Traverse the array from the last digit
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                // If the current digit is less than 9, increment it and return the array
                digits[i]++;
                return digits;
            }
            // Set the current digit to 0 if it's 9 (carry over)
            digits[i] = 0;
        }

        // Step 2: If all digits were 9, add an extra 1 at the beginning
        vector<int> result = {1};
        for (int i = 0; i < n; i++) {
            result.push_back(digits[i]);
        }
        
        return result;
    }
};
