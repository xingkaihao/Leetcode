class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for(int i=m; i<m+n; ++i){
            nums1[i]=nums2[i-m];
        }
        sort(nums1.begin(), nums1.begin()+(m+n));
    }
};
/* 思路：通过for循环把nums的有效元素赋给nums1的有效元素后面，
 * 之后用sort函数对nums1进行排序。
 */