class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
    int size = flowerbed.size();

    for (int i = 0; i < size; i++) {
        if (flowerbed[i] == 0) {
            // Check if left and right are empty
            bool leftEmpty = (i == 0) || (flowerbed[i - 1] == 0);
            bool rightEmpty = (i == size - 1) || (flowerbed[i + 1] == 0);

            if (leftEmpty && rightEmpty) {
                flowerbed[i] = 1; // Plant a flower
                count++;

                // If we've planted enough flowers, return true
                if (count >= n) {
                    return true;
                }
            }
        }
    }

    // Check if we could plant enough flowers
    return count >= n;
    
    }
};