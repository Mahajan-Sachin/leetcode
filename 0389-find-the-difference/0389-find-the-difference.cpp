class Solution {
public:
    char findTheDifference(string s, string t) {
        int result = 0;
    
    // XOR all characters in string s
    for (char c : s) {
        result ^= c;
    }
    
    // XOR all characters in string t
    for (char c : t) {
        result ^= c;
    }
    
    // The remaining result is the ASCII value of the added character
    return static_cast<char>(result);
    }
};