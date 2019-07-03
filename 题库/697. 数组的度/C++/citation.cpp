class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int n=nums.size();
        map<int,vector<int>> tmp;
        for(int i=0;i<n;i++)
        {
            tmp[nums[i]].push_back(i);
        }
        int count=0;
        int res=INT_MAX;
        map<int,vector<int>>::iterator it;
        for(it=tmp.begin();it!=tmp.end();it++)
        {
            int m=it->second.size();
            if(m>count)
            {
                count=m;
                res=it->second[m-1]-it->second[0]+1;
            }
            if(m==count)
            {
                res=min(res,it->second[m-1]-it->second[0]+1);
            }
        }
        return res;
    }
};
// 跟python的思路一样