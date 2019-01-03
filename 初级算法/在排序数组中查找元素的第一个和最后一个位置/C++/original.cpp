class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> temp;
        for(int i=0; i<n; ++i){
            if(nums[i] == target) temp.push_back(i);
        }
        if(temp.empty()) return {-1,-1};
        else return {temp[0], temp[temp.size()-1]};
    }
};
// 思路和python一样，不过数组的表达差别很大。