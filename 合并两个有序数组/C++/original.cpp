class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for(int i=m; i<m+n; ++i){
            nums1[i]=nums2[i-m];
        }
        sort(nums1.begin(), nums1.begin()+(m+n));
    }
};
/* ˼·��ͨ��forѭ����nums����ЧԪ�ظ���nums1����ЧԪ�غ��棬
 * ֮����sort������nums1��������
 */