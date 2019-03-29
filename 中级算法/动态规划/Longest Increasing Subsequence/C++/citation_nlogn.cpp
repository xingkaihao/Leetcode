class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size()==0) return 0;
        vector<int> t(1,nums[0]);
        for(int i=1;i<nums.size();++i){
            if(nums[i]>*(t.rbegin())) t.push_back(nums[i]);
            else{
                int l =0 ,h =t.size()-1;
                while(l<=h){
                    int mid =(l+h)/2;
                    if(t[mid]>nums[i]) h =mid-1;
                    else if(t[mid]==nums[i]) {l=mid;break;}
                    else l =mid+1;
                }
                t[l]=nums[i];
            }
        }
        return t.size();
    }
};
/* 思路：动态规划的思想，找到最长的上升子序列，t为当前最大子序列，
 * nums[i]加上一个元素之后，如果后加的元素大于目前t的最大元素，
 * 就直接把该元素加入t中，如果小于t中最大元素，用该元素替换t中对应
 * 位置的一个较大元素，也就是降低t中元素的值大小。最后得到的t就是最长上升子序列
 */