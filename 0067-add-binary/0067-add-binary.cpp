class Solution {
public:
    string addBinary(string a, string b) {
        // Ensure 'a' is the longer string
        if (a.size() < b.size()) {
            swap(a, b);
        }
        
        int carry = 0;
        int n = a.size();
        int m = b.size();
        string result = "";

        // Traverse from the end of both strings
        for (int i = 0; i < n; i++) {
            int bitA = a[n - 1 - i] - '0'; // Get the ith bit from the end of a
            int bitB = i < m ? b[m - 1 - i] - '0' : 0; // Get the ith bit from the end of b or 0 if out of bounds
            int sum = bitA + bitB + carry; // Sum bits and carry
            carry = sum / 2; // Update carry
            result.push_back((sum % 2) + '0'); // Add the binary digit to result
        }

        // Add carry if any
        if (carry) {
            result.push_back('1');
        }

        // Reverse the result to get the correct order
        reverse(result.begin(), result.end());

        return result;
    }
};
