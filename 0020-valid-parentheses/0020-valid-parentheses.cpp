class Solution {
public:
    bool isValid(string s) {
        stack<char>str;
        for(int i=0;i<s.size();i++){
            if(s[i]=='(' || s[i]=='{' || s[i]=='['){
                str.push(s[i]);
            }
            else{
                 // Ensure stack is not empty before accessing top()
                if (str.empty()) return false; //it is very important otherwise compilers throw error
                if(s[i]==')' && str.top()!='(' ||s[i]=='}' && str.top()!='{' || s[i]==']' && str.top()!='['){
                    return false; // means not in symmetric means wrong order
                }
                str.pop();
            }
              
        }
        return str.empty();
    }
};