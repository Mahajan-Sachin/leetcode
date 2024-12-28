class Solution {
public:
    vector<vector<int>> generate(int row) {
        vector<vector<int>>pascal; //2d vector
        for(int i=0;i<row;i++){
            vector<int>row;
            for(int j=0;j<=i;j++){
                if(j==0 || j==i){
                    row.push_back(1);
                }
                else{
                    vector<int>prev=pascal[i-1];
                    row.push_back(prev[j-1]+prev[j]);
                }
            }
            pascal.push_back(row);
        }
        return pascal;
    }
};