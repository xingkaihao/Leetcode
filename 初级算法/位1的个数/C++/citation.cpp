
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count=0;
        while(n>0){
            n = n&(n-1);
            count +=1;
        }
        return count;
    }
};
// ˼·��ͨ��n��n-1��λ�룬ȥ��n�����һ��1���0��count��������