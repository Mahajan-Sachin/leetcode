class Solution {
public:
void mergeAndSort(vector<int>&arr,int start,int mid,int end){
        int left=mid-start+1;
        int right=end-mid;
        int* Left=new int[left];
        int* Right=new int[right];
        for(int i=0;i<left;i++){
            Left[i]=arr[start+i];
        }
        for(int i=0;i<right;i++){
            Right[i]=arr[mid+1+i];
        }
        int i = 0, j = 0, k = start;
        while(i<left && j<right){
            if(Left[i]<Right[j]){
                arr[k]=Left[i];
                i++;
            }
            else{
                arr[k]=Right[j];
                j++;
            }
            k++;
        }
        while(i<left){
            arr[k]=Left[i];
            i++;
            k++;
        }
        while(j<right){
            arr[k]=Right[j];
            j++;
            k++;
        }
}
void divideAndConquer(vector<int>&arr,int start,int end){
    if (start >= end) {
            return;  // Base case, no need to split further if it's a single element or empty array
        }
    if(start<end){
        int mid = start + (end - start) / 2;
        divideAndConquer(arr,start,mid);
        divideAndConquer(arr,mid+1,end);
        mergeAndSort(arr,start,mid,end);
    }
}
    vector<int> sortArray(vector<int>& nums) {
        divideAndConquer(nums,0,nums.size()-1);
        return nums;
    }
};