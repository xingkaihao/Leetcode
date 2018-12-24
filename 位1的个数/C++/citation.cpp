
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
// 思路：通过n和n-1按位与，去把n的最后一个1变成0，count做计数器