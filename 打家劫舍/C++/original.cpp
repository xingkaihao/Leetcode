class Solution {
public:
    int rob(vector<int>& nums) {
        int now = 0;
        int last = 0;
        for(int i=0; i<nums.size(); ++i){
            int temp = now;
            if(last+nums[i]>now) now = last+nums[i];
            last = temp;
        }
        return now;
    }
};
//思路和python一样