class Solution {
public:
    int hammingDistance(int x, int y) {
        int n = x^y;
        int count=0;
        while(n>0){
            n = n&(n-1);
            count +=1;
        }
        return count;
    }
};
/* x��y��λ������������ֶ�Ӧ������λ��ͬ��λ����1��
 * ͨ��n��n-1��λ�룬����1�ĸ���
 */