#include <iostream>
#include <vector>
#include <string>
using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    if (strs.empty()) return "";  // Return empty string if input is empty

    // Use the first string as reference
    string prefix = strs[0];

    // Compare with each string in the list
    for (int i = 1; i < strs.size(); i++) {
        int j = 0;
        // Compare characters until they mismatch or end of one string is reached
        while (j < prefix.size() && j < strs[i].size() && prefix[j] == strs[i][j]) {
            j++;
        }
        // Update the prefix with the matched part
        prefix = prefix.substr(0, j);
        if (prefix == "") return "";  // No common prefix found
    }
    return prefix;
}

int main() {
    vector<string> strs1 = {"flower", "flow", "flight"};
    vector<string> strs2 = {"dog", "racecar", "car"};

    cout << "Longest Common Prefix (1): " << longestCommonPrefix(strs1) << endl;  // Output: "fl"
    cout << "Longest Common Prefix (2): " << longestCommonPrefix(strs2) << endl;  // Output: ""

    return 0;
}
