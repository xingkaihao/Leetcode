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
/* ˼·����vectorȥ��¼��Ӧλ�õ�nums��������������г��ȣ��ö�̬�滮��˼�룬
 * nums[i]��ĩβ����һ��Ԫ��֮�󣬸�Ԫ�ص�������������г�����֮ǰ��һ������
 * �����г��ȼ�1�����߾���1��
 */