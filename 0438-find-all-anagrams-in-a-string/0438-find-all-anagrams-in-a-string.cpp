class Solution {
public:
    vector<int> findAnagrams(string text, string pat) {
        unordered_map<char,int>window,pattern;
        int i=0,j=0;
        for(auto ch:pat){
            pattern[ch]++;
        }
        vector<int>arr;
        int k=pat.size();
        while(j<text.size()){
            window[text[j]]++;
            if(j-i+1<k){
                j++;
            }
            else if(j-i+1==k){
                if(window==pattern){
                    arr.push_back(i);
                }
                if(window[text[i]]==1){
                    window.erase(text[i]);
                }
                else{
                    window[text[i]]--;
                }
                i++;
                j++;
            }
        }
        return arr;
    }
};