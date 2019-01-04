class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        int i = 0, j = 0, k = 0, target = 0;
        sort(nums.begin(),nums.end());  //对数组进行排序
        for(i = 0; i < nums.size(); i ++){
            if(nums[i] > 0)
                break;
            else if(i > 0 && nums[i] == nums[i - 1])     //跳过重复元素
                continue;
            target = -nums[i];  //更新target，转换为两数之和为target的问题
            j = i+1;
            k = nums.size() -1;
            while(j < k){                
                if(nums[j] + nums[k] == target){
                    result.push_back({nums[i],nums[j],nums[k]});
                    while(nums[j + 1] == nums[j] && j < k) ++j; //跳过重复元素
                    while(nums[k - 1] == nums[k] && j< k) --k;  //跳过重复元素
                    ++j, --k;
                }
                else if(nums[j] + nums[k] > target)
                    --k;
                else
                    ++j;
            }
        }
        return result;
    }
};
/* 三数之和就相当于两数之和的target的是变化的，所以先排序（从小到大），然后遍历数组，
 *获取target（注意去除重复元素），然后对该元素右侧的所有元素求两数之和为target的组合（注意去除重复元素）。
 */