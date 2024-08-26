class Solution {
public:
    int gcd(int a,int b){
        if(b==0) return a;
        return gcd(b,a%b);
    }
    int findGCD(vector<int>& arr) {
        int max=INT_MIN;
        int min=INT_MAX;
        for(int i=0;i<arr.size();i++){
             if (arr[i] > max) {
                max = arr[i];
            }
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return gcd(min,max);
    }
};