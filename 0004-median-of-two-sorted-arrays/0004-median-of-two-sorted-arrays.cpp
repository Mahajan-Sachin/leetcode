class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
         // Ensure nums1 is the smaller array
    if (nums1.size() > nums2.size()) {
        swap(nums1, nums2);
    }

    int m = nums1.size(), n = nums2.size();
    int left = 0, right = m;

    while (left <= right) {
        int partition1 = (left + right) / 2;
        int partition2 = (m + n + 1) / 2 - partition1;

        // Get the maximum and minimum elements around the partitions
        int maxLeft1 = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
        int minRight1 = (partition1 == m) ? INT_MAX : nums1[partition1];

        int maxLeft2 = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
        int minRight2 = (partition2 == n) ? INT_MAX : nums2[partition2];

        // Check if we found a valid partition
        if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
            // If the total length is odd, return the max of left elements
            if ((m + n) % 2 == 1) {
                return max(maxLeft1, maxLeft2);
            } else {
                // If the total length is even, return the average of the max of left elements and the min of right elements
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
            }
        } else if (maxLeft1 > minRight2) {
            // If maxLeft1 is too big, move the partition in nums1 to the left
            right = partition1 - 1;
        } else {
            // If maxLeft2 is too big, move the partition in nums1 to the right
            left = partition1 + 1;
        }
    }

    throw invalid_argument("Input arrays are not sorted.");
    }
};