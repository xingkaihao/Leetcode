class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> nums;
        if(numRows==0) return nums;
        vector<int> nums1;
        nums1.push_back(1);
        nums.push_back(nums1);
        if(numRows==1) return nums;       
        for(int i=2; i<=numRows; ++i){
            nums1.clear();
            nums1.push_back(1);
            for(int j=0; j<i-2; ++j){
                nums1.push_back(nums[i-2][j]+nums[i-2][j+1]);
            }
            nums1.push_back(1);
            nums.push_back(nums1);
        }
        return nums;
    }
};
// 思路和python一样