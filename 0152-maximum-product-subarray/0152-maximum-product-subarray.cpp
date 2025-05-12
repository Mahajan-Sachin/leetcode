class Solution {
public:
    int maxProduct(vector<int>& arr) {
        int currProduct=1,maxi=INT_MIN;
        for(int i=0;i<arr.size();i++){
            currProduct=currProduct*arr[i];
            maxi=max(currProduct,maxi);
            if(currProduct==0){
                currProduct=1;
            }
             
        }
        currProduct=1;
        for(int i=arr.size()-1;i>=0;i--){
            currProduct*=arr[i];
            maxi=max(maxi,currProduct);
            if(currProduct==0){
                currProduct=1;
            }
        }
        return maxi;
    }
};