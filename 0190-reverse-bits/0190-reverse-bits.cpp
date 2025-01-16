class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0; // Initialize the result to 0
    for (int i = 0; i < 32; i++) {
        // Extract the least significant bit
        uint32_t bit = n & 1;
        // Shift result left and add the bit
        result = (result << 1) | bit;
        // Shift input right to process the next bit
        n >>= 1;
    }
    return result;
    }
};