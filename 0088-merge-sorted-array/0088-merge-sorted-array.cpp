class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;  // Pointer for nums1 (last valid element)
        int j = n - 1;  // Pointer for nums2 (last element)
        int k = m + n - 1;  // Pointer for the last position in nums1

        // Merge the arrays in reverse order
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];  // Place the larger element at the end
            } else {
                nums1[k--] = nums2[j--];  // Place the larger element at the end
            }
        }

        // If there are any elements left in nums2, copy them
        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }

        // No need to handle nums1 because they are already in place
    }
};
