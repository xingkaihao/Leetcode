class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int res = 0, mx = 0, n = nums.size();
        vector<int> len(n, 1);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j] && len[i] < len[j] + 1) {
                    len[i] = len[j] + 1;
                }
            }
            mx = max(mx, len[i]);
        }
        return mx;
    }
};
/* 思路：用vector去记录对应位置的nums的最大上升子序列长度，用动态规划的思想，
 * nums[i]的末尾加入一个元素之后，该元素的最大上升子序列长度是之前的一个上升
 * 子序列长度加1，或者就是1。
 */