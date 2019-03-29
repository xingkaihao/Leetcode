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
/* ˼·����̬�滮��˼�룬�ҵ�������������У�tΪ��ǰ��������У�
 * nums[i]����һ��Ԫ��֮�������ӵ�Ԫ�ش���Ŀǰt�����Ԫ�أ�
 * ��ֱ�ӰѸ�Ԫ�ؼ���t�У����С��t�����Ԫ�أ��ø�Ԫ���滻t�ж�Ӧ
 * λ�õ�һ���ϴ�Ԫ�أ�Ҳ���ǽ���t��Ԫ�ص�ֵ��С�����õ���t���������������
 */