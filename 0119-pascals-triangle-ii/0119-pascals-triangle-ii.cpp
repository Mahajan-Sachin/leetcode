class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> pascal; // Vector to store all rows
        for (int i = 0; i <= rowIndex; i++) { // Loop for each row (include rowIndex itself)
            vector<int> ans; // Vector to store the current row
            for (int j = 0; j <= i; j++) { // Loop for each element in the row
                if (j == 0 || j == i) { // First and last elements of the row are always 1
                    ans.push_back(1);
                } else { 
                    // Add the two numbers directly above in Pascal's Triangle
                    ans.push_back(pascal[i - 1][j - 1] + pascal[i - 1][j]);
                }
            }
            pascal.push_back(ans); // Add the current row to the Pascal's Triangle
        }
        return pascal[rowIndex]; // Return the row at rowIndex
    }
};
