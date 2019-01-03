class Solution {
public:
    string countAndSay(int n) {
        if(n==1) return "1";
        if(n==2) return "11";
        string st="11";
        int num;
        string s;
        for(int i=0; i<n-2; ++i){
            string sts="";
            int flag=0;
            int m=st.size();
            for(int j=1; j<m; ++j){
                if(st[j]!=st[j-1]){
                    num=j-flag;
                    s=st[flag];
                    sts+=std::to_string(num)+s;
                    flag=j;
                }
                if(j==m-1){
                    num=j-flag+1;
                    s=st[flag];
                    sts+=std::to_string(num)+s;
                }
            }
            st=sts;
        }
        return st;
    }
};
// 跟python的程序思路一样