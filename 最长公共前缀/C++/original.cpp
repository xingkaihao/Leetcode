class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty()) return "";
        int n = strs.size();
        string temp = strs[0];
        for(int i = 1; i < n; ++i){
            if(!strs[i].size()) return "";
            
            int ns = strs[i].size();
            int nt = temp.size();
            int m;
            if(ns <= nt) m = ns;
            else m = nt;
            
            for(int j = 0; j < m; ++j){
                if(temp[j] != strs[i][j]){
                    temp = temp.substr(0, j);
                    break;
                }
                if(j+1 == m) temp = temp.substr(0, j+1);
            }
        }
        return temp;
    }
};
// 和python程序思路一样