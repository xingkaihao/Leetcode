class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        int i = 0, j = 0, k = 0, target = 0;
        sort(nums.begin(),nums.end());  //�������������
        for(i = 0; i < nums.size(); i ++){
            if(nums[i] > 0)
                break;
            else if(i > 0 && nums[i] == nums[i - 1])     //�����ظ�Ԫ��
                continue;
            target = -nums[i];  //����target��ת��Ϊ����֮��Ϊtarget������
            j = i+1;
            k = nums.size() -1;
            while(j < k){                
                if(nums[j] + nums[k] == target){
                    result.push_back({nums[i],nums[j],nums[k]});
                    while(nums[j + 1] == nums[j] && j < k) ++j; //�����ظ�Ԫ��
                    while(nums[k - 1] == nums[k] && j< k) --k;  //�����ظ�Ԫ��
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
/* ����֮�;��൱������֮�͵�target���Ǳ仯�ģ����������򣨴�С���󣩣�Ȼ��������飬
 *��ȡtarget��ע��ȥ���ظ�Ԫ�أ���Ȼ��Ը�Ԫ���Ҳ������Ԫ��������֮��Ϊtarget����ϣ�ע��ȥ���ظ�Ԫ�أ���
 */