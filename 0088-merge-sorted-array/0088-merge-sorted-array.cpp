class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int k = m + n;  // The total size of the merged array
        vector<int> arr(k);  // Create a new array to store the merged result

        // Copy elements from nums1 to arr
        for (int i = 0; i < m; i++) {
            arr[i] = nums1[i];
        }

        // Copy elements from nums2 to arr, starting from where nums1 ends
        for (int j = 0; j < n; j++) {
            arr[m + j] = nums2[j];
        }

        // Now sort the new array
        sort(arr.begin(), arr.end());

        // Copy the merged and sorted array back to nums1
        for (int i = 0; i < k; i++) {
            nums1[i] = arr[i];
        }
    }
};
