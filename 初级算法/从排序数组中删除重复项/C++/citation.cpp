class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }   
        int number = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[number] != nums[i]) {
                number ++;
                nums[number] = nums[i];
            }
        }
        return (number + 1);
    }
};
/* 思路：首先判断nums是否为空。利用双指针去完成题目，快指针遍历
 * 整个nums，慢指针把副本后移，number+1为移除副本后的数值新长度
 */