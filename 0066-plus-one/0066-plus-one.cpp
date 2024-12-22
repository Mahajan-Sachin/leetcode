class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        string num = "";
        // Convert the array of digits into a string
        for (int digit : digits) {
            num += (digit + '0'); // Convert integer to char
        }

        // Perform addition from the last digit
        int carry = 1;
        for (int i = num.size() - 1; i >= 0; i--) {
            int sum = (num[i] - '0') + carry; // Convert char to int
            num[i] = (sum % 10) + '0';        // Update digit in string
            carry = sum / 10;                 // Update carry
        }

        // If there's a carry left, prepend '1'
        if (carry) {
            num.insert(num.begin(), '1');
        }

        // Convert the string back to a vector of integers
        vector<int> result;
        for (char c : num) {
            result.push_back(c - '0'); // Convert char to int
        }
        return result;
    }
};
