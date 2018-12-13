class Solution {
public:
    int climbStairs(int n) {
        vector<int> s;
        s.push_back(1);
        s.push_back(2);
        if(n==1) return 1;
        if(n==2) return 2;
        for(int i=2; i<n; i++){
            s.push_back(s[i-1]+s[i-2]);
        }
        return s[n-1];
    }
};
//使用斐波那契数列，很完美。