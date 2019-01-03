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
/* x和y按位异或，这两个数字对应二进制位不同的位置置1，
 * 通过n和n-1按位与，计算1的个数
 */